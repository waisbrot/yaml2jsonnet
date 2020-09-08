from typing import Any

from ruamel.yaml import YAML

from yaml2jsonnet.jsonnet_renderer import JsonnetRenderer


def convert_yaml(
    yaml_data: str, output: Any, array=True, inject_comments=False
) -> None:
    yaml = YAML(typ="rt")
    yaml.version = "1.1"  # type: ignore  # yaml.version is mis-typed as None
    events = yaml.parse(yaml_data)
    JsonnetRenderer(events, output, array, inject_comments).render()
