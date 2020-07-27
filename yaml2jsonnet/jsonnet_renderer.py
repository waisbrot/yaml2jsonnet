import functools
import logging
import re

from ruamel.yaml.events import (
    DocumentEndEvent,
    DocumentStartEvent,
    MappingEndEvent,
    MappingStartEvent,
    ScalarEvent,
    SequenceEndEvent,
    SequenceStartEvent,
    StreamEndEvent,
    StreamStartEvent,
)

re_true: re.Pattern = re.compile(r"(?:true|yes|on)", re.IGNORECASE)
re_false = re.compile(r"(?:false|no|off)", re.IGNORECASE)
re_unescaped_key = re.compile(r"[a-zA-Z][a-zA-Z0-9]*")
re_newline_comment = re.compile(r"^\s*[\n\r]\s*#")

log = logging.getLogger(__name__)


class RenderConversionError(RuntimeError):
    def __init__(self, renderer, msg, event):
        self.message = msg
        self.event = event
        self.queue = renderer.queue
        self.state = renderer.state
        super().__init__(msg)

    def __str__(self):
        return f"{self.message}: Last event was {self.event}, the state was {self.state.__name__}, the queue was {self.queue}"


class UnhandledEventError(RenderConversionError):
    def __init__(self, renderer, event):
        super().__init__(renderer, "Event was not handled by the current state", event)


class WrongStateOnPop(RenderConversionError):
    def __init__(self, renderer, expected, event):
        super().__init__(
            renderer,
            f"Did not get the expected state {expected} on the top of the queue",
            event,
        )


def prime(func):
    """Prime a consumer by calling it once on creation"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        f = func(*args, **kwargs)
        next(f)
        return f

    return wrapper


class PDQueue(list):
    def __str__(self):
        return (
            "["
            + ", ".join(
                [
                    "(" + i[0].__class__.__name__ + "," + i[1].__name__ + ")"
                    for i in self
                ]
            )
            + "]"
        )

    def __repr__(self):
        return self.__str__()


class JsonnetRenderer:
    def __init__(self, events, output):
        self.events = events
        self.output = output
        self.queue = PDQueue()
        self.state = None
        self.s_start = self._start()
        self.s_stream = self._stream()
        self.s_document = self._document()
        self.s_sequence = self._sequence()
        self.s_mapping_key = self._mapping_key()
        self.s_mapping_value = self._mapping_value()
        self.current_document = []
        self.document_count = 0
        self.trailing_comments = []

    def really_write(self, string):
        self.output.write(string)

    def write_current_document(self):
        [self.really_write(s) for s in self.current_document]
        self.current_document = []

    def write_trailing_comments(self):
        [self.write(comment) for comment in self.trailing_comments]
        self.trailing_comments = []

    def write(self, string):
        self.current_document.append(string)

    def remove_trailing_comma(self):
        self.current_document[-1] = self.current_document[-1].rstrip(",\n ")

    def queue_comment(self, comment):
        if comment is None:
            return
        if isinstance(comment, list):
            return [self.queue_comment(c) for c in comment]
        comment = comment.value.rstrip()
        if re_newline_comment.match(comment):
            self.trailing_comments.append("\n")
        comment = comment.lstrip(" #\t\n\r")
        self.trailing_comments.append("//")
        self.trailing_comments.append(comment)
        self.trailing_comments.append("\n")

    def render(self):
        self.state = self.s_start
        for event in self.events:
            log.debug(
                f"current state = {self.state.__name__}; current event = {event}; current queue = {self.queue}\n"
            )
            if event.comment is not None:
                self.queue_comment(event.comment[0])
                self.queue_comment(event.comment[1])
            self.state.send(event)

    def render_scalar(self, scalar: str) -> None:
        try:
            self.write(repr(int(scalar)))
            return
        except ValueError:
            pass
        try:
            self.write(repr(float(scalar)))
            return
        except ValueError:
            pass
        if re_true.fullmatch(scalar):
            self.write("true")
        elif re_false.fullmatch(scalar):
            self.write("false")
        else:
            self.write(repr(scalar))

    def render_map_key(self, scalar: str) -> None:
        if re_unescaped_key.fullmatch(scalar):
            self.write(scalar)
        else:
            self.write("[" + repr(scalar) + "]")

    def pop_state(self, expectedPrior, event):
        prior = self.queue.pop()
        if not isinstance(prior[0], expectedPrior):
            raise WrongStateOnPop(self, expectedPrior, event)
        self.state = prior[1]

    @prime
    def _start(self):
        while True:
            event = yield
            if isinstance(event, StreamStartEvent):
                self.queue.append((event, self.state))
                self.state = self.s_stream
                # Render a stream as a Jsonnet list
                self.write("/* top-level stream of documents */\n")
            else:
                raise UnhandledEventError(self, event)

    @prime
    def _stream(self):
        while True:
            event = yield
            if isinstance(event, DocumentStartEvent):
                if self.document_count > 0:
                    self.really_write("[")  # prepend a list
                    self.write(",")
                    self.write_current_document()
                self.document_count += 1
                self.queue.append((event, self.state))
                self.state = self.s_document
                self.write(f"/* document {self.document_count}*/\n")
                self.write_trailing_comments()
            elif isinstance(event, StreamEndEvent):
                self.pop_state(StreamStartEvent, event)
                self.write_current_document()
                if self.document_count > 1:
                    self.really_write("]\n")
            else:
                raise UnhandledEventError(self, event)

    @prime
    def _document(self):
        while True:
            event = yield
            if isinstance(event, SequenceStartEvent):
                self.queue.append((event, self.state))
                self.state = self.s_sequence
                self.write("[\n")
                self.write_trailing_comments()
            elif isinstance(event, MappingStartEvent):
                self.queue.append((event, self.state))
                self.state = self.s_mapping_key
                self.write("{\n")
                self.write_trailing_comments()
            elif isinstance(event, DocumentEndEvent):
                self.remove_trailing_comma()
                self.pop_state(DocumentStartEvent, event)
            else:
                raise UnhandledEventError(self, event)

    @prime
    def _sequence(self):
        while True:
            event = yield
            if isinstance(event, ScalarEvent):
                self.render_scalar(event.value)
                self.write(",")
                self.write_trailing_comments()
            elif isinstance(event, SequenceEndEvent):
                self.pop_state(SequenceStartEvent, event)
                self.write_trailing_comments()
                self.write("],\n")
            elif isinstance(event, MappingStartEvent):
                self.queue.append((event, self.state))
                self.state = self.s_mapping_key
                self.write("{\n")
                self.write_trailing_comments()
            else:
                raise UnhandledEventError(self, event)

    @prime
    def _mapping_key(self):
        while True:
            event = yield
            if isinstance(event, ScalarEvent):
                self.render_map_key(event.value)
                self.write(":")
                self.state = self.s_mapping_value
            elif isinstance(event, MappingEndEvent):
                self.pop_state(MappingStartEvent, event)
                self.write_trailing_comments()
                self.write("},\n")
            else:
                raise UnhandledEventError(self, event)

    @prime
    def _mapping_value(self):
        while True:
            event = yield
            if isinstance(event, ScalarEvent):
                self.render_scalar(event.value)
                self.write(",")
                self.write_trailing_comments()
                self.state = self.s_mapping_key
            elif isinstance(event, MappingStartEvent):
                self.queue.append(
                    (event, self.s_mapping_key)
                )  # return to the mapping _key_ state, not value
                self.state = self.s_mapping_key
                self.write("{\n")
                self.write_trailing_comments()
            elif isinstance(event, SequenceStartEvent):
                self.queue.append(
                    (event, self.s_mapping_key)
                )  # return to the mapping _key_ state, not value
                self.state = self.s_sequence
                self.write("[\n")
                self.write_trailing_comments()
            else:
                raise UnhandledEventError(self, event)
