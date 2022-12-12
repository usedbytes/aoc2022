#!/usr/bin/env python3
import sys

grid = []

# First build the grid
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()

        if 'S' in line:
            start = (line.index('S'), len(grid))

        if 'E' in line:
            end = (line.index('E'), len(grid))

        grid.append([ord(c) - ord('a') for c in line])

grid[start[1]][start[0]] = 0
grid[end[1]][end[0]] = 25

def grid_v(pos):
    return grid[pos[1]][pos[0]]

dirs = {
        (0, -1): '^',
        (1, 0): '>',
        (0, 1): 'v',
        (-1, 0): 'v',
}

nrows = len(grid)
ncols = len(grid[0])

paths = {}
goals = []

def visit(pos, path):
    if (pos in paths) and len(paths[pos]) <= len(path):
        return []

    paths[pos] = path
    cur_height = grid_v(pos)

    if (cur_height == 0) and (pos not in goals):
        goals.append(pos)

    nexts = []

    for d in dirs:
        next_pos = (pos[0] + d[0], pos[1] + d[1])

        if next_pos[0] < 0 or next_pos[0] >= ncols:
            continue

        if next_pos[1] < 0 or next_pos[1] >= nrows:
            continue

        next_height = grid_v(next_pos)

        # Working backwards - we can only step up, or down-by-1
        if next_height >= (cur_height - 1):
            new_path = path.copy()
            new_path.append(d)

            nexts.append((next_pos, new_path))

    return nexts

to_visit = [(end, [])]

while len(to_visit) > 0:
    pos, path = to_visit.pop()

    to_visit.extend(visit(pos, path))

print("Part 1:", len(paths[start]))

print("Part 2:", min([len(paths[g]) for g in goals]))
