#!/usr/bin/env python3
import sys

sn2v = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2,
}

v2sn = {
    2: '2',
    1: '1',
    0: '0',
    -1: '-',
    -2: '=',
}

numbers = []

def snafu2int(snafu):
    num = 0
    for c in snafu:
        v = sn2v[c]
        num *= 5
        num += v
    return num

def int2snafu(num):
    digits = []
    while num != 0:
        unit = 5
        v = num % unit    
        num //= 5
        if v > 2:
            num += 1
            v = v - 5
        digits.insert(0, v2sn[v])
    return ''.join(digits)

with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        numbers.append(snafu2int(line))

print("Part 1:", int2snafu(sum(numbers)))

