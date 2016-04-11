#!/usr/bin/env python

with open("output.txt", "r+") as f:
    lines = f.readlines()
    f.seek(0)
    for line in lines:
        if len(line) > 2:
            line = line[:-3] + chr(ord(line[-2]) + 1) + line[-2:]
        f.write(line)
