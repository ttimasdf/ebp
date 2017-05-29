#!/usr/bin/env python3
"""
Uni-patcher is a program which would patch (even large) binary
efficiently based on binary fingerprints.
"""

from uni_patcher import config, options, logging
from uni_patcher.patcher import Patcher
from os.path import exists

def main():
    args = options.get_args()
    log = logging.get_logger(__package__, args.verbose)

    if not exists(args.conf_file):
        log.critical("Cannot find config file, exiting...")
        return 1

    conf = config.parse_file(args.conf_file)
    m = conf['metadata']

    print("""
=================={len}====
    Uni-patcher @ {name}
=================={len}====

{desc}
""".format(
    name=m['name'],
    len='='*len(m['name']),
    desc=m["description"],
    ))

    for name, info in conf['files'].items():
        log.info("Patching {}...".format(name))

        p = Patcher(info, basedir=args.source, test=args.test)

        if p.unsign:
            log.error("NotImplemented: automatic unsign")

        p.patch()

    print("""
Done!

Advice from author:

{congrat}
""".format(congrat=m['congratulation']))
    log.info("Patch completed successfully!")

if __name__ == '__main__':
    main()
