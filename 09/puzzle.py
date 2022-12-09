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

def dump_knots(hpos, knots):
    print(knots)
    pts = [(0,0)]
    pts.extend(knots)
    pts.extend([hpos])

    print("")
    minx = min([v[0] for v in pts])
    maxx = max([v[0] for v in pts])
    miny = min([v[1] for v in pts])
    maxy = max([v[1] for v in pts])
    xr = (maxx - minx) + 1
    yr = (maxy - miny) + 1

    grid = [['.'] * xr for i in range(yr + 1)]
    grid[0 - miny][0 - minx] = 's'
    grid[hpos[1] - miny][hpos[0] - minx] = 'H'
    for i in range(len(knots)):
        k = knots[i]
        grid[k[1] - miny][k[0] - minx] = str(i + 1)

    for row in grid:
        print(' '.join(row))

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
                        dy = diff[1] // abs(diff[1])
                elif diff[0] > 1:
                    dx = 1
                    if diff[1] != 0:
                        dy = diff[1] // abs(diff[1])
                elif diff[1] < -1:
                    dy = -1
                    if diff[0] != 0:
                        dx = diff[0] // abs(diff[0])
                elif diff[1] > 1:
                    dy = 1
                    if diff[0] != 0:
                        dx = diff[0] // abs(diff[0])

                knots[i] = (knot[0] + dx, knot[1] + dy)
                kif = knots[i]

            if len(sys.argv) > 2:
                dump_knots(hpos, knots[:i+1])

            p1[knots[0]] = True
            p2[knots[-1]] = True

print("Part 1:", len(p1))
print("Part 2:", len(p2))
