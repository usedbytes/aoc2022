#!/usr/bin/env python3
import sys

def run(lines, inspect):
    cycle = 1
    X = 1

    for line in lines:
        if cycle in inspect:
            inspect[cycle] = X

        if line == "noop":
            cycle += 1
        elif line.startswith("addx"):
            _, count = line.split()
            count = int(count)
            cycle += 1
            if cycle in inspect:
                inspect[cycle] = X
            cycle += 1
            X += count
    if cycle in inspect:
        inspect[cycle] = X

lines = []
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        lines.append(line)

inspect = {}
for i in range(20, 220+1, 40):
    print(i)
    inspect[i] = 0

run(lines, inspect)

strength = sum([k * v for k, v in inspect.items()])
print("Part 1:", strength)
