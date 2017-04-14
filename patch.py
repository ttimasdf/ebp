#!/usr/bin/env python3

from pathlib import Path
import subprocess
import mmap
import logging

logger = logging.getLogger('uni-patcher')
logger.setLevel('DEBUG')

fingerprints = [
    (1, b'bytes')  # (offset_to_anchor, expected_bytes)
]

sub = (b'orig', b'subs')  # (original_bytes, substituted_bytes) -- same length!
def main(*argv):
    if len(argv) >= 2:
        app_path = Path(argv[1])
        if '-d' in argv or '--dry-run' in argv:
            logger.info("Running in the sky (-d)")
            dry_run = True
        else:
            dry_run = False
    else:
        print("usage: patch <appdir> [-d/--dry-run]")
        return -1

    blob_path = app_path/'Contents'/'MacOS'/'Sublime Text'  # as example

    if not blob_path.exists():
        logger.error("Required executable not exists")
        return -1

    f = blob_path.open('r+b')
    mm = mmap.mmap(f.fileno(), 0)  # , access=mmap.ACCESS_COPY)
    logging.info("Mapping file {}".format(blob_path))

    anchor = mm.find(sub[0])
    while anchor > 0:
        logger.debug("Match at position {}".format(anchor))
        for fg in fingerprints:
            target = anchor + fg[0]
            if mm[target:target+len(fg[1])] == fg[1]:
                logger.debug("Fingerprint {} match!".format(fingerprints.index(fg)))
                match = True
            else:
                logger.debug("Fingerprint {} unmatch!".format(fingerprints.index(fg)))
                logger.debug("Purposed: {} Actual: {}".format(fg[1], mm[target:target+len(fg[1])]))
                match = False
                break
        if match:
            logging.info("Patching bytes at position {}")
            if input("Continue?(y/n)") == 'y' and not dry_run:
                mm[anchor:anchor+len(sub[0])] = sub[1]
            break
        anchor = mm.find(sub[0], anchor+1)

    logging.info("Finished successfully!")
    mm.flush()

if __name__ == '__main__':
    from sys import argv
    main(*argv)
