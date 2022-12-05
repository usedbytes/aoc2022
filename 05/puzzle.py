#!/usr/bin/env python3

import copy
import sys

stacks = []
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip('\n')
        if line.startswith(" 1"):
            break

        stack = 0
        i = 0
        while i < len(line):
            entry = line[i:i+4]
            entry = entry.strip(" []")
            if len(stacks) <= stack:
                stacks.append([])
            if len(entry) == 1:
                stacks[stack].append(entry)
            i += 4
            stack += 1

    stacks2 = copy.deepcopy(stacks)

    for line in f:
        line = line.strip()
        if len(line) == 0:
            continue

        parts = line.split()
        count, src, dst = int(parts[1]), int(parts[3])-1, int(parts[5])-1

        # Part 1
        for i in range(count):        
            v = stacks[src].pop(0)
            stacks[dst].insert(0, v)

        # Part 2
        vs = copy.copy(stacks2[src][:count])
        stacks2[src] = stacks2[src][count:]
        vs.extend(stacks2[dst])
        stacks2[dst] = vs

vals = [stack[0] for stack in stacks]
print("Part 1:", ''.join(vals))
vals = [stack[0] for stack in stacks2]
print("Part 2:", ''.join(vals))
