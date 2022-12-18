#!/usr/bin/env python3
import sys

min_x = None
max_x = 0
min_y = None
max_y = 0
min_z = None
max_z = 0

occupied = {}

with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()

        x, y, z = [int(v) for v in line.split(',')]

        occupied[(x,y,z)] = True

        if min_x is None or x < min_x:
            min_x = x
        if min_y is None or y < min_y:
            min_y = y
        if min_z is None or z < min_z:
            min_z = z

        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        if z > max_z:
            max_z = z

ds = [
    (  1,  0,  0 ),
    ( -1,  0,  0 ),
    (  0,  1,  0 ),
    (  0, -1,  0 ),
    (  0,  0,  1 ),
    (  0,  0, -1 ),
]

part1 = 0
for k, v in occupied.items():
    for d in ds:
        pos = (k[0] + d[0], k[1] + d[1], k[2] + d[2])
        if pos not in occupied:
            part1 += 1

print("Part 1:", part1)

touching_water = {}
def touches_water(pos, visited = []):
    if pos in touching_water:
        ans = touching_water[pos]
        for v in visited:
            touching_water[v] = ans
        return ans

    visited.append(pos)

    if ((pos[0] < min_x) or (pos[0] > max_x) or
        (pos[1] < min_y) or (pos[1] > max_y) or
        (pos[2] < min_z) or (pos[2] > max_z)):
        touching_water[pos] = True
        for v in visited:
            touching_water[v] = True
        return True

    for d in ds:
        v = (pos[0] + d[0], pos[1] + d[1], pos[2] + d[2])
        if v in visited:
            continue

        if v in occupied:
            continue

        if touches_water(v, visited.copy()):
            return True

    for v in visited:
        touching_water[v] = False
    return False

part2 = 0
for k, v in occupied.items():
    for d in ds:
        pos = (k[0] + d[0], k[1] + d[1], k[2] + d[2])
        if pos not in occupied and touches_water(pos, []):
            part2 += 1

print("Part 2:", part2)
