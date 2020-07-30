import sys

from yaml2jsonnet.cli import parse_args


def test_parse_args() -> None:
    args = parse_args(["test/yaml/list1.yaml", "--out", "-", "-vv"])
    assert args.yaml.name == "test/yaml/list1.yaml"
    assert args.out == sys.stdout
    assert args.v == 2
