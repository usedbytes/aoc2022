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

# Find the cube side length
min_w = len(grid)
max_len = 0
for line in grid:
    n_cells = len(line) - line.count(' ')
    min_w = min(min_w, n_cells)
    max_len = max(max_len, len(line))

for c in range(max_len):
    n_cells = 0
    for r in range(len(grid)):
        line = grid[r]
        if c < len(line) and line[c] != ' ':
            n_cells += 1
    min_w = min(min_w, n_cells)

sides = {}
side_coords = []

print("min_w:", min_w)
side_length = min_w
for r in range(0, len(grid), side_length):
    for c in range(0, max_len, side_length):
        print((c, r))
        line = grid[r]
        print(line, len(line))
        print(' ' * c + '^')
        if c <= (len(line) - side_length) and line[c] != ' ':
            side = [grid[r + i][c:c+side_length] for i in range(side_length)]
            x = c // side_length
            y = r // side_length
            sides[(x, y)] = side
            side_coords.append((x, y))
            print(f'Add side {(x, y)}')
            for line in side:
                print(line)

assert(len(sides) == 6)
print(sides.keys())
