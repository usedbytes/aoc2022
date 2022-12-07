#!/usr/bin/env python3
import sys

lines = []
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip('\n')
        lines.append(line)

cwd = ['']
cwd_self_size = 0
dirs = {}

i = 0
# First calculate a self size for each directory
# We'll identify directories by the tuple of their path
while i < len(lines):
    line = lines[i]
    if line.startswith('$'):
        parts = line[2:].split()

        if parts[0] == 'cd':
            cwd_self_size = 0
            if parts[1] == '/':
                cwd = ['']
            elif parts[1] == '..':
                cwd = cwd[:-1]
            else:
                cwd.append(parts[1])
            i += 1
        elif parts[0] == 'ls':
            # Parse ls output, calculate self size
            i += 1
            while i < len(lines):
                line = lines[i]
                if line.startswith('$'):
                    break

                parts = line.split()
                if parts[0] == 'dir':
                    pass
                else:
                    cwd_self_size += int(parts[0])
                i += 1
            # Store the self size
            dirs[tuple(cwd)] = cwd_self_size
    else:
        print(line)
        assert(False)

# Add each dir's self size to its anscestors' sizes
for k, v in dirs.items():
    for i in range(0, len(k)-1):
        dirs[tuple(k[0:i+1])] += v

# Total up the ones smaller than 100k
totals = []
for v in dirs.values():
    if v < 100000:
        totals.append(v)
print("Part 1:", sum(totals))
