#!/usr/bin/env python3
import sys

dirs = {
    "R": ( 1,  0),
    "L": (-1,  0),
    "U": ( 0, -1),
    "D": ( 0,  1),
}

hpos = (0, 0)
tpos = (0, 0)
positions = {}
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        parts = line.split()
        d = dirs[parts[0]]
        c = int(parts[1])
        for i in range(c):
            hpos = (hpos[0] + d[0], hpos[1] + d[1])
            diff = (hpos[0] - tpos[0], hpos[1] - tpos[1])

            dx = 0
            dy = 0

            if diff[0] < -1:
                dx = -1
                if diff[1] != 0:
                    dy = diff[1]
            elif diff[0] > 1:
                dx = 1
                if diff[1] != 0:
                    dy = diff[1]

            if diff[1] < -1:
                dy = -1
                if diff[0] != 0:
                    dx = diff[0]
            elif diff[1] > 1:
                dy = 1
                if diff[0] != 0:
                    dx = diff[0]

            tpos = (tpos[0] + dx, tpos[1] + dy)
            positions[tpos] = True

print("Part 1:", len(positions))
