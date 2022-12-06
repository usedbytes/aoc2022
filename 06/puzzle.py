#!/usr/bin/env python3
import sys

with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip('\n')

        i = 3
        while i <= len(line):
            buf = line[i-3:i+1]
            uniques = set(buf)
            if len(uniques) == 4: 
                print("Part 1:", i + 1)
                break
            i += 1
