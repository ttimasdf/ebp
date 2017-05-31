# Extensive Binary Patcher
EBP can patch a binary, just tell it where and how. Optionally, it can remove the signature from a macho-format executable.


# Usage
```
usage: ebpatcher [-h] [-c CONF_FILE] [-r] [-t] [-v] source

EBP is a program which would patch (even large) binary efficiently
based on binary fingerprints.

positional arguments:
  source                Base directory from config file

optional arguments:
  -h, --help            show this help message and exit
  -c CONF_FILE, --config CONF_FILE
                        Configuration file
  -r, --reverse         Revert files using backups
  -t, --test, --dry-run
                        Verify only
  -v, --verbose         Output more information for diagnostic
```

# Config file format
```
[metadata]
name=Patch name
description=Print before applying patch
congratulation=Print after applying the patch

[patch:what_ever_the_name]
unsign=true
file=relative/path/from/basedir

# Relative patches format(one entry per line, indented):
# SRC,DST,(FINGERPRINT_POS,EXPECTED_DATA)+
relatives=
    DEADBEEF,FEEDCAFEBEEF,1,CAFE
    FEADBEEF,DEEDBEEF,-1,CAFF,3,CAFE

# Fixed position patches format:
# POS,SRC,DST
absolutes=
    65536,FEEDFACE,FEEDFACF
```
