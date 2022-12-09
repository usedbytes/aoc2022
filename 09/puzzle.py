#!/usr/bin/env python3
import sys

dirs = {
    "R": ( 1,  0),
    "L": (-1,  0),
    "U": ( 0, -1),
    "D": ( 0,  1),
}

hpos = (0,0)
knots = [(0,0) for i in range(9)]

p1 = {}
p2 = {}
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        parts = line.split()
        d = dirs[parts[0]]
        c = int(parts[1])

        for i in range(c):
            hpos = (hpos[0] + d[0], hpos[1] + d[1])

            # knot in front
            kif = hpos

            for i in range(len(knots)):
                knot = knots[i]
                diff = (kif[0] - knot[0], kif[1] - knot[1])

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

                knots[i] = (knot[0] + dx, knot[1] + dy)
                kif = knots[i]

            p1[knots[0]] = True
            p2[knots[-1]] = True

print("Part 1:", len(p1))
print("Part 2:", len(p2))
