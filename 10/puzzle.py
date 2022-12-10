#!/usr/bin/env python3
import sys

def run(lines, cycle_consumers):
    cycle = 1
    X = 1

    for line in lines:
        for c in cycle_consumers:
            c(cycle, X)

        if line == "noop":
            cycle += 1
        elif line.startswith("addx"):
            _, count = line.split()
            count = int(count)
            cycle += 1
            for c in cycle_consumers:
                c(cycle, X)
            cycle += 1
            X += count

    for c in cycle_consumers:
        c(cycle, X)

lines = []
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        lines.append(line)

part1 = {}
def part1_consumer(cycle, X):
    if cycle in range(20, 220+1, 40):
        part1[cycle] = X

part2 = []
def part2_consumer(cycle, X):
    if cycle in range(1, 240+1, 40):
        part2.append(['.'] * 40)

    crt_pos = (cycle - 1)  % 40
    if crt_pos in [X-1, X, X+1]:
        part2[-1][crt_pos] = '#'

run(lines, [part1_consumer, part2_consumer])

strength = sum([k * v for k, v in part1.items()])
print("Part 1:", strength)

print("Part 2:")
for row in part2:
    print(''.join(row))
