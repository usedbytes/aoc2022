#!/usr/bin/env python3

import sys

overlap_entirely = []
overlap_at_all = []
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        parts = line.split(',')

        e1parts = parts[0].split("-")
        e1 = (int(e1parts[0]), int(e1parts[1]))
        e2parts = parts[1].split("-")
        e2 = (int(e2parts[0]), int(e2parts[1]))

        isect = (max(e1[0], e2[0]), min(e1[1], e2[1]))

        if (isect[0] <= isect[1]):
            overlap_at_all.append((e1, e2, isect))
            if ((e1[0] >= isect[0] and e1[1] <= isect[1]) or
                (e2[0] >= isect[0] and e2[1] <= isect[1])):
                overlap_entirely.append((e1, e2, isect))

print("Part 1:", len(overlap_entirely))
print("Part 2:", len(overlap_at_all))
