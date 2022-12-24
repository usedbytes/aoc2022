#!/usr/bin/env python3
import sys
import re

elves = {}

with open(sys.argv[1]) as f:
    for r, line in enumerate(f):
        line = line.strip('\n')

        for c, v in enumerate(line):
            if v == '#':
                elves[(c, r)] = True

move_num = 0

dirs = [
    [(0, -1), (1, -1), (-1, -1)], # n_ne_nw
    [(0, 1), (1, 1), (-1, 1)],    # s_se_sw
    [(-1, 0), (-1, -1), (-1, 1)], # w_nw_sw
    [(1, 0), (1, -1), (1, 1)],    # e_ne_se
]

adj = [
    (0, -1), (1, -1),
    (1, 0), (1, 1),
    (0, 1), (-1, 1),
    (-1, 0), (-1, -1),
]

def propose(pos, move_num):
    has_adjacent = False
    for a in adj:
        np = (pos[0] + a[0], pos[1] + a[1])
        if np in elves:
            has_adjacent = True
            break
    if not has_adjacent:
        return pos

    for dir_num in range(len(dirs)):
        checks = dirs[(move_num + dir_num) % len(dirs)]
        should_move = True
        for d in checks:
            np = (pos[0] + d[0], pos[1] + d[1])
            if np in elves:
                should_move = False
                break
        if should_move:
            return (pos[0] + checks[0][0], pos[1] + checks[0][1])

for move in range(10):
    proposals = {}
    for e in elves:
        p = propose(e, move)
        if p in proposals:
            proposals[p].append(e)
        else:
            proposals[p] = [e]

    new_elves = {}
    for k, v in proposals.items():
        if len(v) == 1:
            new_elves[k] = True
        else:
            for e in v:
                new_elves[e] = True
    elves = new_elves

min_x = None
min_y = None
max_x = 0
max_y = 0
for e in elves:
    if min_x is None or e[0] < min_x:
        min_x = e[0]
    if min_y is None or e[1] < min_y:
        min_y = e[1]
    max_x = max(max_x, e[0])
    max_y = max(max_y, e[1])
ntiles = (max_x - min_x + 1) * (max_y - min_y + 1)

print("Part 1:", ntiles - len(elves))
