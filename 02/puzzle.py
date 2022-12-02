#!/usr/bin/env python3
import sys

infile = sys.argv[1]

scores = {
    ('A', 'X'): 1 + 3,
    ('A', 'Y'): 2 + 6,
    ('A', 'Z'): 3 + 0,

    ('B', 'X'): 1 + 0,
    ('B', 'Y'): 2 + 3,
    ('B', 'Z'): 3 + 6,

    ('C', 'X'): 1 + 6,
    ('C', 'Y'): 2 + 0,
    ('C', 'Z'): 3 + 3,
}

moves = {
    ('A', 'X'): 'Z',
    ('A', 'Y'): 'X',
    ('A', 'Z'): 'Y',

    ('B', 'X'): 'X',
    ('B', 'Y'): 'Y',
    ('B', 'Z'): 'Z',

    ('C', 'X'): 'Y',
    ('C', 'Y'): 'Z',
    ('C', 'Z'): 'X',
}

part1_score = 0
part2_score = 0
with open(infile) as f:
    for line in f:
        line = line.strip()
        them, me = line.split()
        part1_score += scores[(them, me)]

        # Change my move based on the new strategy
        me = moves[(them, me)]
        part2_score += scores[(them, me)]

print("Part 1:", part1_score)
print("Part 2:", part2_score)
