#!/usr/bin/env python3
import sys

polylines = []
minx = 1e6
maxx = 0
miny = 0
maxy = 0

# Parse the input and determine the size of the grid
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        parts = line.split(' -> ')
        poly = []
        for p in parts:
            x, y = p.split(',')
            x = int(x)
            y = int(y)
            minx = min(x, minx)
            maxx = max(x, maxx)
            miny = min(y, miny)
            maxy = max(y, maxy)
            poly.append((x, y))
        polylines.append(poly)

# HAX: Just expand by a huge amount to try and not run out of space
minx -= 300
maxx += 300

if len(sys.argv) > 2:
    maxy += 2
    polylines.append([(minx, maxy), (maxx, maxy)])

nx = maxx - minx + 1
ny = maxy - miny + 1

# Create a grid full of 'air'
grid = [['.'] * nx for i in range(ny)]

# Draw in all the rock
for pl in polylines:
    for i in range(len(pl)-1):
        if pl[i][0] == pl[i+1][0]:
            # Vertical
            x = pl[i][0] - minx
            start = min(pl[i+1][1], pl[i][1]) - miny
            end = max(pl[i+1][1], pl[i][1]) - miny
            for j in range(start, end + 1):
                grid[j][x] = '#'
        elif pl[i][1] == pl[i+1][1]:
            # Horizontal
            y = pl[i][1] - miny
            start = min(pl[i+1][0], pl[i][0]) - minx
            end = max(pl[i+1][0], pl[i][0]) - minx
            for j in range(start, end + 1):
                grid[y][j] = '#'

# Sand source
grid[0][500 - minx] = '+'

def grid_v(pos):
    return grid[pos[1] - miny][pos[0] - minx]

def grid_set(pos, v):
    grid[pos[1] - miny][pos[0] - minx] = v

# Simulate sand
i = 0
while True:
    pos = (500, 0)
    i += 1
    while True:
        if pos[1] >= maxy:
            break
        elif len(sys.argv) > 2 and pos[1] >= maxy - 1:
            break
        elif grid_v((pos[0], pos[1]+1)) == '.':
            pos = (pos[0], pos[1]+1)
        elif grid_v((pos[0]-1, pos[1]+1)) == '.':
            pos = (pos[0]-1, pos[1]+1)
        elif grid_v((pos[0]+1, pos[1]+1)) == '.':
            pos = (pos[0]+1, pos[1]+1)
        else:
            break
    grid_set(pos, 'o')
    if pos[1] >= maxy:
        break
    if pos == (500, 0):
        break

for row in grid:
    print(''.join(row))
print('')

if len(sys.argv) <= 2:
    print("Part 1:", i-1)
else:
    print("Part 2:", i)
