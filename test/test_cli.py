from yaml2jsonnet.cli import parse_args


def test_parse_args() -> None:
    parse_args(["test/yaml/list1.yaml"])
