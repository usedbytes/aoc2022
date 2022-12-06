#!/usr/bin/env python3
import sys

def find_marker(line, length):
    i = length - 1
    while i <= len(line):
        buf = line[i-(length - 1):i+1]
        uniques = set(buf)
        if len(uniques) == length:
            return i + 1
        i += 1
    return -1

with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip('\n')

        p1 = find_marker(line, 4)
        print("Part 1:", p1)
        p2 = find_marker(line, 14)
        print("Part 2:", p2)
