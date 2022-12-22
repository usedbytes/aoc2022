#!/usr/bin/env python3
import sys
import re

grid = []

with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip('\n')
        if line == '':
            break

        grid.append(line)

    for line in f:
        line = line.strip()
        path = line

def get_instr(path):
    if path[0].isnumeric():
        i = 0
        while i < len(path) and path[i].isnumeric():
            i += 1
        steps = int(path[:i])
        return steps, path[i:]

    return path[0], path[1:]


r = 0
c = grid[0].index('.')
facing = 0
facings = '>v<^'

dirs = [
    ( 1,  0),
    ( 0,  1),
    (-1,  0),
    ( 0, -1),
]

while len(path) > 0:
    instr, path = get_instr(path)

    if isinstance(instr, int):
        d = dirs[facing]
        while instr > 0:
            next_c, next_r = (c + d[0], r + d[1])

            # Wrap to top
            if (next_r > 0) and ((next_r > len(grid)-1) or (c > len(grid[next_r])) or (grid[next_r][c] == ' ')):
                next_r = 0
                while True:
                    if (len(grid[next_r]) > c) and grid[next_r][c] != ' ':
                        break
                    next_r += 1
            # Wrap to bottom
            elif (next_r < 0) or (c > len(grid[next_r])) or (grid[next_r][c] == ' '):
                next_r = len(grid)-1
                while True:
                    if (len(grid[next_r]) > c) and grid[next_r][c] != ' ':
                        break
                    next_r -= 1
            # Wrap to left
            elif next_c > len(grid[r])-1:
                next_c = grid[r].index('.')
                if next_c == -1:
                    next_c = grid[r].index('#')

            # Wrap to right
            if next_c < 0 or grid[r][next_c] == ' ':
                next_c = grid[r].rindex('.')
                if next_c == -1:
                    next_c = grid[r].rindex('#')

            if grid[next_r][next_c] == '#':
                # Wall
                break

            c, r = next_c, next_r
            instr -= 1
    else:
        cur = facing
        if instr == 'R':
            cur += 1
        elif instr == 'L':
            cur -= 1
        cur %= len(facings)
        facing = cur

print("Part 1:", (1000 * (r + 1)) + (4 * (c + 1)) + facing)
