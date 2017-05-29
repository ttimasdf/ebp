from argparse import ArgumentParser, FileType

desc = """Uni-patcher is a program which would patch (even large) binary
efficiently based on binary fingerprints.
"""

_parser = ArgumentParser(prog=__package__, description=desc)

_parser.add_argument("-c", "--config",
    dest="conf_file", help="Configuration file")
_parser.add_argument("-u", "--unsign",
    action="store_true", help="Unsign executable if needed")
_parser.add_argument("-r", "--reverse",
    action="store_true", help="Revert files using backups")
_parser.add_argument("-t", "--test", "--dry-run",
    action="store_true", help="Verify only")
_parser.add_argument("-v", "--verbose",
    action="store_true", help="Output more information for diagnostic")
_parser.add_argument("source", help="Base directory from config file")


def get_args(args=None):
    return _parser.parse_args(args)
