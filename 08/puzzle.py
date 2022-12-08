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

# Scenic scores
scores = []
for row in range(nrows):
    scores.append([0] * ncols)
    for col in range(ncols):
        tree = grid[row][col]

        dirs = [
            [ 1,  0], # Eastwards
            [-1,  0], # Westwards
            [ 0, -1], # Northwards
            [ 0,  1], # Southwards
        ]

        score = 1
        for d in dirs:
            col2 = col
            row2 = row
            i = 0
            while True:
                col2 += d[0]
                row2 += d[1]
                if col2 < 0 or col2 > (ncols - 1):
                    break
                if row2 < 0 or row2 > (nrows - 1):
                    break

                i += 1

                if grid[row2][col2] >= tree:
                    break
            score *= i
        scores[row][col] = score

print("Part 2:", max([max(row) for row in scores]))
