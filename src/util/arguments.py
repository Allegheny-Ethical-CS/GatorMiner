"""Handle the arguments"""
import argparse


def parse(args):
    """Use argparse to parse provided command-line arguments"""
    # create the parser with the default help formatter
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog="""Sample usage: python3 textmining.py --directory
            /Users/myname/projectdirectory""",
    )

    # add all of the arguments to the command-line interface
    parser.add_argument(
        "--directory",
        required=False,
        type=str,
        help="Directory with mardown documents to analyze",
    )

    # parse the arguments and return the finished result
    arguments_finished = parser.parse_args(args)
    return arguments_finished
