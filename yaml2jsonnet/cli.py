"""Functions for helping run from the command line"""

import argparse
import logging
import sys
from typing import Sequence

from yaml2jsonnet.yaml2jsonnet import convert_yaml

log = logging.getLogger(__name__)


def parse_args(args: Sequence[str] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="yaml2jsonnet",
        description="Convert a YAML file to a JSONNET file, preserving comments",
    )
    parser.add_argument("yaml", type=argparse.FileType("r"))
    parser.add_argument("--out", default=sys.stdout, type=argparse.FileType("w"))
    parser.add_argument("-v", action="count", default=0)

    return parser.parse_args(args)


def run(args: argparse.Namespace) -> None:
    log.debug("Read yaml into memory")
    yaml_data = args.yaml.read()
    convert_yaml(yaml_data, args.out)


def main() -> None:
    args = parse_args()
    loglevel = logging.WARNING
    if args.v > 0:
        loglevel = logging.INFO
    if args.v > 1:
        loglevel = logging.DEBUG
    logging.basicConfig(level=loglevel)
    run(args)
