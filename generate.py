#!/usr/bin/env python

N = 150

with open("output.txt", "w") as f:
    for idx in range(1,N):
        f.write(" ".join(["aaa"]*idx) + "\n")
