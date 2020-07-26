from ruamel.yaml import YAML


def fib(n: int) -> int:
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def read_yaml(yaml_data: str) -> object:
    yaml = YAML()
    return yaml.load(yaml_data)
