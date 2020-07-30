from io import StringIO
from json import loads

from _gojsonnet import evaluate_snippet
from ruamel.yaml import events

from yaml2jsonnet.jsonnet_renderer import JsonnetRenderer


def test_mapping_states():
    """Test some transitions around maps"""
    output = StringIO()
    renderer = JsonnetRenderer([], output)
    renderer.state = renderer.s_document
    renderer.state.send(events.MappingStartEvent(None, None, None))
    assert renderer.state == renderer.s_mapping_key
    renderer.state.send(events.ScalarEvent(None, None, None, "hello"))
    assert renderer.state == renderer.s_mapping_value
    renderer.state.send(events.ScalarEvent(None, None, None, "world"))
    assert renderer.state == renderer.s_mapping_key
    renderer.state.send(events.ScalarEvent(None, None, None, "foo"))
    assert renderer.state == renderer.s_mapping_value
    renderer.state.send(events.MappingStartEvent(None, None, None))
    assert renderer.state == renderer.s_mapping_key
    renderer.state.send(events.ScalarEvent(None, None, None, "bar"))
    assert renderer.state == renderer.s_mapping_value
    renderer.state.send(events.ScalarEvent(None, None, None, "baz"))
    assert renderer.state == renderer.s_mapping_key
    renderer.state.send(events.MappingEndEvent(None, None, None))
    assert renderer.state == renderer.s_mapping_key


def test_simple_list():
    """Test that we can get a list through to JSON"""
    event_list = [
        events.StreamStartEvent(),
        events.DocumentStartEvent(),
        events.SequenceStartEvent(None, None, None),
        events.ScalarEvent(None, None, None, "hello"),
        events.ScalarEvent(None, None, None, "world"),
        events.SequenceEndEvent(),
        events.DocumentEndEvent(),
        events.StreamEndEvent(),
    ]
    output = StringIO()
    JsonnetRenderer(event_list, output, False).render()
    json = evaluate_snippet(src=output.getvalue(), filename="")
    data = loads(json)
    assert len(data) == 2
    assert data[0] == "hello"
    assert data[1] == "world"
