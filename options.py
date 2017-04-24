from main import __doc__ as desc
import util
from argparse import ArgumentParser, FileType


parser = ArgumentParser(description=desc)

parser.add_argument("-c", "--conf",
    dest="conf_file", help="Configuration file")
parser.add_argument("-u", "--unsign",
    action="store_true", default=False, help="Unsign executable if needed")
parser.add_argument("-d", "--dry-run", "--verify",
    action="store_true", default=False, help="Verify only")
parser.add_argument("source",
    action=FileType("rb"), help="Source file to patch")
parser.add_argument("dest",
    action=FileType("r+b"), nargs="?", help="Destination file")

