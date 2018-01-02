import argparse
from datetime import datetime
import time

def base_parser(description: str) -> argparse.ArgumentParser:

    parser = argparse.ArgumentParser(description=description, add_help=True)
    parser.add_argument("--output", action="store",
                        help="Path in which to store result. Can be local or S3.")

    parser.add_argument("--timestamp", action="store_true",
                        help="If true, append the timestamp to the output path.")

    parser.add_argument("--partitions", type=int, action="store",
                        help="Number of partitions to use for core process.")

    parser.add_argument("--timeout", type=int, action="store",
                        help="Number of seconds for each filing before giving up.",
                        default = 10)

    parser.add_argument("--no-timeout", action="store_true",
                        help="If true, don't time out for any filings.")

    return parser

def get_output_path(args):
    if args.timestamp:
        timestamp = datetime.fromtimestamp(time.time()).strftime(
            '%Y-%m-%d-%H-%M-%S')
        suffix = "/%s" % timestamp
    else:
        suffix = ""

    outputPath = args.output + suffix
    return outputPath

def input_arg(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    parser.add_argument("--input", action="append",
                        help="Path to input file(s). Can supply multiple.")

    return parser

def target_column(parser: argparse.ArgumentParser, default=None) -> argparse.ArgumentParser:
    if default is not None:
        parser.add_argument("--target-column", action="store",
                            help="Column on which to perform transformation.",
                            default=default)
    else:
        parser.add_argument("--target-column", action="store",
                            help="Column on which to perform transformation.")

    return parser
