from io import StringIO
from json import loads

from _gojsonnet import evaluate_snippet

from yaml2jsonnet.yaml2jsonnet import convert_yaml


def test_convert_yaml_array() -> None:
    input = "hello: world"
    output = StringIO()
    convert_yaml(input, output, array=True)
    json = evaluate_snippet(src=output.getvalue(), filename="")
    parsed_json = loads(json)
    assert len(parsed_json) == 1
    assert "hello" in parsed_json[0]
    assert parsed_json[0]["hello"] == "world"


def test_convert_yaml_dict() -> None:
    input = "hello: world"
    output = StringIO()
    convert_yaml(input, output, array=False)
    json = evaluate_snippet(src=output.getvalue(), filename="")
    parsed_json = loads(json)
    assert "hello" in parsed_json
    assert parsed_json["hello"] == "world"
