#!/usr/bin/env python

N = 500

with open("output.txt", "w") as f:
    for idx in range(1,N):
        f.write("a"*idx + "\n")
