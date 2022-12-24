#!/usr/bin/env python3
import sys
from collections import defaultdict

blizzards = defaultdict(list)

y = 0
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip('\n')
        if line.count('#') > 2:
            continue

        for x, c in enumerate(line):
            if c in ">v<^":
                blizzards[(x-1, y)].append(c)
        y += 1

start = (0, -1)
end = (len(line) - 3, y)

def move_blizzards(blizzards):
    new_blizzards = defaultdict(list)
    for k, lv in blizzards.items():
        for v in lv:
            nx = k[0]
            ny = k[1]
            if v == '>':
                nx = nx + 1
                if nx > end[0]:
                    nx = 0
            elif v == '<':
                nx = nx - 1
                if nx < 0:
                    nx = end[0]
            elif v == 'v':
                ny = ny + 1
                if ny >= end[1]:
                    ny = 0
            elif v == '^':
                ny = ny - 1
                if ny < 0:
                    ny = end[1] - 1
            #print(f'{k} -> {(nx, ny)}')
            new_blizzards[(nx, ny)].append(v)
    return new_blizzards

def print_blizzards(blizzards):
    for y in range(end[1]):
        row = []
        for x in range(end[0]+1):
            lv = blizzards.get((x, y), [])
            if len(lv) > 1:
                row.append(str(len(lv)))
            elif len(lv) == 1:
                row.append(lv[0])
            else:
                row.append('.')
        print(''.join(row))

dirs = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
    (0, 0),
]

to_visit = [(start, [])]

while True and len(to_visit) > 0:
    blizzards = move_blizzards(blizzards)
    next_visit = {}
    for v, p in to_visit:
        for d in dirs:
            pos = (v[0] + d[0], v[1] + d[1])

            if pos == end:
                print("Part 1:", len(p) + 1)
                exit()

            if (pos != (0, -1)) and (pos[0] < 0 or pos[1] < 0):
                continue

            if pos[0] > end[0] or pos[1] > end[1] - 1:
                continue

            if pos in blizzards:
                continue

            path = p.copy()
            path.append(pos)
            cur_best = next_visit.get(pos, None)
            if cur_best is None or len(path) < len(cur_best):
                next_visit[pos] = path

    to_visit = [(k, v) for k, v in next_visit.items()]

