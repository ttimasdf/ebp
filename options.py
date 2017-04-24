from .main import __doc__ as desc
from argparse import ArgumentParser, Action


class Options(ArgumentParser):
    "OptionParser specifically for Project"

    def __init__(self):
        super().__init__(description=desc)
        self.add_argument("-c", "--conf",
            dest="conf_file", help="Configuration file")
        self.add_argument("-u", "--unsign",
            action="store_true", default=False, help="Unsign executable if needed")
        self.add_argument("-d", "--dry-run", "--verify",
            action="store_true", default=False, help="Verify only")
        self.add_argument("src",
            required=True, help="Source file to patch")
        self.add_argument("dst",
            nargs="?", help="Destination file")

