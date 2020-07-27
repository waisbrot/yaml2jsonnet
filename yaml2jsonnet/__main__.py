import logging

from yaml2jsonnet.cli import parse_args, run

if __name__ == "__main__":
    args = parse_args()
    loglevel = logging.WARNING
    if args.v > 0:
        loglevel = logging.INFO
    if args.v > 1:
        loglevel = logging.DEBUG
    logging.basicConfig(level=loglevel)
    run(args)
