"""
EBP is a program which would patch (even large) binary
efficiently based on binary fingerprints.
"""

from . import config, options, logging
from .patcher import Patcher
from os.path import exists
import shutil
from unsign.unsign import unsign_macho


def main():
    args = options.get_args()
    log = logging.get_logger(__package__, args.verbose)

    if not exists(args.conf_file):
        log.critical("Cannot find config file, exiting...")
        raise SystemExit

    conf = config.parse_file(args.conf_file)
    m = conf['metadata']

    print("""
=========={len}====
    EBP @ {name}
=========={len}====

{desc}
""".format(
        name=m['name'],
        len='=' * len(m['name']),
        desc=m["description"],
    ))

    for name, info in conf['files'].items():
        log.info("Patching {}...".format(name))

        p = Patcher(info, basedir=args.source, test=args.test)
        target = p.file.parent / (p.file.name + config.BACKUP_SUFFIX)
        if target.exists():
            log.warning("Backup file {} already exists".format(target))
        else:
            shutil.copyfile(p.file, target)
            log.debug("Backed up to {}".format(target))

        if p.unsign:
            unsign_macho(p.file.open('r+b'))
            log.info("Unsign {} completed".format(name))

        p.patch()

    print("""
Done!

Advice from author:

{congrat}
""".format(congrat=m['congratulation']))
    log.info("Patch completed successfully!")
