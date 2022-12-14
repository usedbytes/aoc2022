#!/usr/bin/env python3
import sys
from functools import cmp_to_key

pairs = []

a = None
b = None
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        if len(line) == 0:
            pairs.append((a, b))
            a = None
            b = None
        elif a is None:
            a = eval(line)
        elif b is None:
            b = eval(line)
    pairs.append((a, b))

def compare(a, b):
    #print(f'compare({a}, {b})')
    res = __compare(a, b)
    #print(f'res({a}, {b}) -> {res}')
    return res

def __compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0
    elif isinstance(a, int) and isinstance(b, list):
        return compare([a], b)
    elif isinstance(a, list) and isinstance(b, int):
        return compare(a, [b])
    else:
        l = min(len(a), len(b))
        for i in range(l):
            res = compare(a[i], b[i])
            if res == 0:
                continue
            else:
                return res
        if len(a) < len(b):
            return -1
        elif len(a) > len(b):
            return 1
        else:
            return 0

part1 = 0
for i in range(len(pairs)):
    p = pairs[i]
    res = compare(p[0], p[1])
    if res < 0:
        part1 += (i + 1)

print("Part 1:", part1)

packets = []
for p in pairs:
    packets.append(p[0])
    packets.append(p[1])

ordered = sorted(packets, key=cmp_to_key(compare))
dividers = [
    [[2]],
    [[6]],
]

part2 = 1
for d in dividers:
    for i in range(len(ordered)):
        p = ordered[i]
        res = compare(d, p)
        if res < 0:
            part2 *= (i + 1)
            ordered.insert(i, d)
            break

print("Part 2:", part2)
