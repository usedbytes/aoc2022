#!/usr/bin/env python3
import sys

sensor_beacons = {}
sensor_distances = {}
beacons = []

with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        parts = line.split()

        sx = int(parts[2].strip("x=,"))
        sy = int(parts[3].strip("y=:"))
        bx = int(parts[8].strip("x=,"))
        by = int(parts[9].strip("y="))

        sensor = (sx, sy)
        beacon = (bx, by)
        sensor_beacons[sensor] = beacon
        beacons.append(beacon)

        distance = abs(sx - bx) + abs(sy - by)
        sensor_distances[sensor] = distance

y = 10
xlimit = 20
ylimit = 20
if len(sys.argv) > 2:
    y = 2000000
    ylimit = 4000000
    xlimit = 4000000

part1 = {}
for s, d in sensor_distances.items():
    vdist = abs(y - s[1])
    width = d - vdist
    for x in range(s[0] - width, s[0] + width + 1):
        if (x, y) not in beacons and (x, y) not in sensor_distances:
            part1[(x, y)] = True
print("Part 1:", len(part1))

def search(xlimit, ylimit):
    y = 0
    while y < ylimit:
        x = 0
        while x < xlimit:
            pos = (x, y)
            for s, d in sensor_distances.items():
                vdist = abs(y - s[1])
                width = d - vdist
                if s[0] - width - 1 < x <= s[0] + width:
                    x = s[0] + width + 1
                    continue
            if (x, y) == pos:
                return pos
        y += 1
    return None

pos = search(xlimit, ylimit)
print("Part 2:", pos[0] * 4000000 + pos[1])
