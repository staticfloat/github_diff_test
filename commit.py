#!/usr/bin/env python

with open("output.txt", "r+") as f:
    lines = f.readlines()
    f.seek(0)
    for line in lines:
        if len(line) > 8:
            line = line[:-8] + chr(ord(line[-7]) + 1) + line[-7:]
        f.write(line)
