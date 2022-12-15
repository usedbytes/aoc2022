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
if len(sys.argv) > 2:
    y = int(sys.argv[2])

part1 = {}
for s, d in sensor_distances.items():
    vdist = abs(y - s[1])
    width = d - vdist
    for x in range(s[0] - width, s[0] + width + 1):
        if (x, y) not in beacons and (x, y) not in sensor_distances:
            part1[(x, y)] = True
print(len(part1))
