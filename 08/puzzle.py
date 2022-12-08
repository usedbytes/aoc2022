#!/usr/bin/env python3
import sys

grid = []
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip('\n')
        grid.append([int(v) for v in line])

# Use a dictionary to store trees by coordinate, which gives us de-duplication
visible = {}

nrows = len(grid)
ncols = len(grid[0])

# Left to right
for row in range(nrows):
    height = -1
    for col in range(ncols):
        tree = grid[row][col]
        if tree > height:
            visible[(col, row)] = True
            height = tree

# Right to left
for row in range(nrows):
    height = -1
    for col in range(ncols):
        tree = grid[row][ncols-col-1]
        if tree > height:
            visible[(ncols-col-1, row)] = True
            height = tree

# Top to bottom
for col in range(ncols):
    height = -1
    for row in range(nrows):
        tree = grid[row][col]
        if tree > height:
            visible[(col, row)] = True
            height = tree

# Bottom to top
for col in range(ncols):
    height = -1
    for row in range(nrows):
        tree = grid[nrows-row-1][col]
        if tree > height:
            visible[(col, nrows-row-1)] = True
            height = tree

print("Part 1:", len(visible))
