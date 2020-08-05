from io import StringIO
from json import loads
from textwrap import dedent

from _gojsonnet import evaluate_snippet

from yaml2jsonnet.yaml2jsonnet import convert_yaml


def _convert(yaml_in: str, array: bool) -> dict:
    """
    Take a YAML doc in string-form, return the result of
    YAML -> Jsonnet -> JSON -> json.loads()
    """
    output = StringIO()
    convert_yaml(yaml_in, output, array=array)
    json = evaluate_snippet(src=output.getvalue(), filename="")
    return loads(json)


def test_convert_yaml_array() -> None:
    parsed_json = _convert("hello: world", True)
    assert len(parsed_json) == 1
    assert "hello" in parsed_json[0]
    assert parsed_json[0]["hello"] == "world"


def test_convert_yaml_dict() -> None:
    parsed_json = _convert("hello: world", False)
    assert "hello" in parsed_json
    assert parsed_json["hello"] == "world"


def test_quoted_unquoted_true() -> None:
    """Bug I found where I was reading a quote 'true' as a boolean"""
    parsed_json = _convert('---\nhello: "true"\n', False)
    assert "hello" in parsed_json
    assert parsed_json["hello"] == "true"

    parsed_json = _convert("---\nhello: true\n", False)
    assert "hello" in parsed_json
    assert parsed_json["hello"] is True


def test_empty_map() -> None:
    """Bug I found where I was reading an empty map-value as empty-string"""
    parsed_json = _convert(
        dedent(
            """
    ---
    list:
     - one
     - two
    mapA:
      good: yes
    mapB:
    """
        ),
        False,
    )
    assert parsed_json["list"] == ["one", "two"]
    assert parsed_json["mapA"] == {"good": True}
    assert parsed_json["mapB"] is None
