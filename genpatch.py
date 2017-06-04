#!/usr/bin/env python3

import sys
from progressbar import ProgressBar

if len(sys.argv) >= 3:
    orig = sys.argv[1]
    patched = sys.argv[2]
    if len(sys.argv) == 4:
        res = sys.argv[3]
    else:
        res = 'result.txt'
else:
    print("usage: genpatch <orig> <patched> [<patch>]")
    exit(1)

f_orig = open(orig, 'rb')
f_patched = open(patched, 'rb')
f_result = open(res, 'w')

filelen = f_orig.seek(0, 2)
if f_patched.seek(0, 2) != filelen:
    print("File size not identical!")
    exit(1)

f_orig.seek(0)
f_patched.seek(0)

bar = ProgressBar()

result = []

for i in bar(range(filelen)):
    byte_o = f_orig.read(1)
    byte_p = f_patched.read(1)
    if byte_o != byte_p:
        result.append((i, byte_o, byte_p))
        f_result.write("{}: {:02X} {:02X}\n".format(i, byte_o[0], byte_p[0]))
