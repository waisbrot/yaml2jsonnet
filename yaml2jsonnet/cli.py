"""Functions for helping run from the command line"""

import argparse
import sys
from typing import Sequence

from yaml2jsonnet.yaml2jsonnet import read_yaml


def parse_args(args: Sequence[str] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="yaml2jsonnet",
        description="Convert a YAML file to a JSONNET file, preserving comments",
    )
    parser.add_argument("yaml", type=argparse.FileType("r"))
    parser.add_argument("--out", default=sys.stdout, type=argparse.FileType("w"))

    return parser.parse_args(args)


def run(args: argparse.Namespace) -> None:
    yaml_data = args.yaml.read()
    parsed = read_yaml(yaml_data)
    args.out.write(repr(parsed))
