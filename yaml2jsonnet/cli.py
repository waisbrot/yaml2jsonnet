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
    parser.add_argument(
        "yaml", type=argparse.FileType("r"), help="YAML file to convert"
    )
    parser.add_argument(
        "-o",
        "--out",
        default=sys.stdout,
        type=argparse.FileType("w"),
        help="File to write out to (or stdout)",
    )
    parser.add_argument(
        "-c",
        "--document-comments",
        type=bool,
        help="Add comments about which YAML document produced which map",
    )
    parser.add_argument(
        "-v",
        action="count",
        default=0,
        help="Logging verbosity: one for info, two for debug",
    )

    return parser.parse_args(args)


def run(args: argparse.Namespace) -> None:
    log.debug("Read yaml into memory")
    yaml_data = args.yaml.read()
    convert_yaml(yaml_data, args.out, args.document_comments)


def main() -> None:
    args = parse_args()
    loglevel = logging.WARNING
    if args.v > 0:
        loglevel = logging.INFO
    if args.v > 1:
        loglevel = logging.DEBUG
    logging.basicConfig(level=loglevel)
    run(args)
    args.out.close()
