#!/usr/bin/env python

N = 60

with open("output.txt", "w") as f:
    for idx in range(1,N):
        f.write(" ".join(["aaa"]*idx) + "\n")
