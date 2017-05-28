# uni-patcher
It can patch a binary, just tell it where and how.

# Config file format
```
[metadata]
name=Patch name
description=Print before applying patch
congratulation=Print after applying the patch

[patch:what_ever_the_name]
unsign=true

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
