"""
Most of the work of the package -- renders a stream of ruamel events into Jsonnet
"""

import functools
import logging
import re
import textwrap

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

"""Regex for converting YAML true boolean to JSON"""
re_true: re.Pattern = re.compile(r"(?:true|yes|on)", re.IGNORECASE)

"""Regex for converting YAML false boolean to JSON"""
re_false = re.compile(r"(?:false|no|off)", re.IGNORECASE)

re_null = re.compile(r"(?:~|null|Null|NULL|)")

"""Regex for testing if a string can be used as Jsonnet key without escaping"""
re_unescaped_key = re.compile(r"[_a-zA-Z][_a-zA-Z0-9]*")

"""Regex for checking if a comment starts with a newline (starting with a newline
means that it gets a line of its own, instead of being a trailing comment)"""
re_newline_comment = re.compile(r"^\s*[\n\r]\s*#")

"""Regex for replacing Python's default \x0a repr with a unicode version"""
re_low_ascii_replace = re.compile(r"\\x([0-9a-f]{2})")

"""Jsonnet reserved words. Can't use them as map keys.
https://jsonnet.org/ref/spec.html#lexing"""
reserved_words = [
    "assert",
    "else",
    "error",
    "false",
    "for",
    "function",
    "if",
    "import",
    "importstr",
    "in",
    "local",
    "null",
    "tailstrict",
    "then",
    "self",
    "super",
    "true",
]

log = logging.getLogger(__name__)


class RenderConversionError(RuntimeError):
    """Base class for errors when rendering the event-stream into Jsonnet"""

    def __init__(self, renderer, msg, event):
        self.message = msg
        self.event = event
        self.queue = renderer.queue
        self.state = renderer.state
        super().__init__(msg)

    def __str__(self):
        return f"{self.message}: Last event was {self.event}, the state was {self.state.__name__}, the queue was {self.queue}"


class UnhandledEventError(RenderConversionError):
    """The current state doesn't handle the current event. Programmer error."""

    def __init__(self, renderer, event):
        super().__init__(renderer, "Event was not handled by the current state", event)


class WrongStateOnPop(RenderConversionError):
    """The state,event pair being popped off the stack did not match. Programmer error."""

    def __init__(self, renderer, expected, event):
        super().__init__(
            renderer,
            f"Did not get the expected state {expected} on the top of the queue",
            event,
        )


class MultipleDocumentsError(RenderConversionError):
    """Renderer was expecting a single document but got multiple. User error."""

    def __init__(self, renderer, event):
        super().__init__(
            renderer, "Expecting a single document but got multiple", event
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
    """Just a list, but subclassed to give a pretty-printer for debugging"""

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
    """Main class. Represents a deterministic pushdown automoton."""

    def __init__(self, events, output, document_array=True):
        """Most of the initialization is to create consumers for the various states."""
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
        self.document_array = document_array

    def really_write(self, string):
        """Write a string to the output"""
        self.output.write(string)

    def write_current_document(self):
        """Dump the current_document buffer to the output"""
        [self.really_write(s) for s in self.current_document]
        self.current_document = []

    def write_trailing_comments(self):
        """Write any pending comments into to the current_document buffer"""
        [self.write(comment) for comment in self.trailing_comments]
        self.trailing_comments = []

    def write(self, string):
        """Write a string into the current_document buffer"""
        self.current_document.append(string)

    def remove_trailing_comma(self):
        """Strip the trailing comma from the current_document buffer"""
        self.current_document[-1] = self.current_document[-1].rstrip(",\n ")

    def queue_comment(self, comment):
        """Expects the comment attr of an Event. If there are any comments,
        put them into the pending comments queue"""
        if comment is None:
            return
        if isinstance(comment, list):
            return [self.queue_comment(c) for c in comment]
        comment = comment.value.rstrip()
        if re_newline_comment.match(comment):
            self.trailing_comments.append("\n")
        comment = comment.lstrip(" #\t\n\r")
        self.trailing_comments.append("// ")
        self.trailing_comments.append(comment)
        self.trailing_comments.append("\n")

    def render(self) -> None:
        """Begin evaluating, reading from the events and writing to the output until done"""
        self.state = self.s_start
        for event in self.events:
            log.debug(
                f"current state = {self.state.__name__}; current event = {event}; current queue = {self.queue}\n"
            )
            if event.comment is not None:
                self.queue_comment(event.comment[0])
                self.queue_comment(event.comment[1])
            self.state.send(event)

    def render_scalar(self, scalar: str, quoted: bool) -> None:
        """Given a string that might represent a number or boolean, render it to JSON"""
        if not quoted:
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
                return
            elif re_false.fullmatch(scalar):
                self.write("false")
                return
            elif re_null.fullmatch(scalar):
                self.write("null")
                return
        if len(scalar) > 80 and "\n" in scalar:
            self.write("|||\n")
            self.write(textwrap.indent(scalar, " "))
            self.write("\n|||")
        else:
            scalar = repr(scalar)
            scalar = re_low_ascii_replace.sub(r"\\u00" + "\\1", scalar)
            self.write(scalar)

    def render_map_key(self, scalar: str) -> None:
        """Given a string that is a map-key, render it as Jsonnet (maybe escaping it)"""
        if re_unescaped_key.fullmatch(scalar) and scalar not in reserved_words:
            self.write(scalar)
        else:
            scalar = repr(scalar)
            scalar = re_low_ascii_replace.sub(r"\\u00" + "\\1", scalar)
            self.write(f"[{scalar}]")

    def pop_state(self, expectedPrior, event):
        """Pop the top state off the stack. Assert that it is of the expected type"""
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
                if self.document_array:
                    self.write("[\n")
            else:
                raise UnhandledEventError(self, event)

    @prime
    def _stream(self):
        while True:
            event = yield
            if isinstance(event, DocumentStartEvent):
                if self.document_count > 0:
                    if self.document_array:
                        self.write(",")
                        self.write_current_document()
                    else:
                        raise MultipleDocumentsError(self, event)
                self.document_count += 1
                self.queue.append((event, self.state))
                self.state = self.s_document
                self.write(f"/* document {self.document_count}*/\n")
                self.write_trailing_comments()
            elif isinstance(event, StreamEndEvent):
                self.pop_state(StreamStartEvent, event)
                self.write_current_document()
                if self.document_array:
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
                self.render_scalar(event.value, quoted=(event.style is not None))
                self.write(",")
                self.write_trailing_comments()
            elif isinstance(event, SequenceStartEvent):
                self.queue.append((event, self.state))
                self.state = self.s_sequence  # same state we're already in
                self.write("[\n")
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
                self.render_scalar(event.value, quoted=(event.style is not None))
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
