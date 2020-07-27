from typing import Any

from ruamel.yaml import YAML

from yaml2jsonnet.jsonnet_renderer import JsonnetRenderer


def fib(n: int) -> int:
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def convert_yaml(yaml_data: str, output: Any) -> object:
    yaml = YAML(typ="rt")
    yaml.version = "1.1"  # type: ignore  # yaml.version is mis-typed as None
    events = yaml.parse(yaml_data)
    return JsonnetRenderer(events, output).render()
