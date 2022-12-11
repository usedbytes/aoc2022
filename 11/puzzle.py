#!/usr/bin/env python3
import sys

monkey_items = []
monkey_ops = []
monkey_divs = []
monkey_throws = []
monkey_inspections = []

lines = []

def do_one(i):
    item = monkey_items[i].pop(0)

    op = monkey_ops[i]

    a = op[0]
    if a is None:
        a = item
        
    b = op[2]
    if b is None:
        b = item

    if op[1] == '+':
        item = a + b
    elif op[1] == '*':
        item = a * b
    else:
        assert(False)

    monkey_inspections[i] += 1

    # Reduce worry level
    item = item // 3

    if item % monkey_divs[i] == 0:
        monkey_items[monkey_throws[i][0]].append(item)
    else:
        monkey_items[monkey_throws[i][1]].append(item)

with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        lines.append(line)

i = 0
while i < len(lines): 
        line = lines[i]
        if len(line) == 0:
            pass
        elif line.startswith("Monkey"):
            monkey_inspections.append(0)
            pass
        elif line.startswith("Starting items:"):
            line = line[len("Starting items: "):]
            parts = line.split(', ')
            parts = [int(v) for v in parts]
            monkey_items.append(parts)
        elif line.startswith("Operation:"):
            line = line[len("Operation: "):]

            parts = line.split()
            assert(parts[0] == 'new')
            assert(parts[1] == '=')

            a = parts[2]
            if a == 'old':
                a = None
            else:
                a = int(a)

            op = parts[3]

            b = parts[4]
            if b == 'old':
                b = None
            else:
                b = int(b)

            monkey_ops.append((a, op, b))

        elif line.startswith("Test:"):
            line = line[len("Test: divisible by "):]
            monkey_divs.append(int(line))

            if_true = lines[i+1].split()[-1]
            if_false = lines[i+2].split()[-1]
            monkey_throws.append((int(if_true), int(if_false)))
            i += 2
        i += 1

for rnd in range(20):
    for i in range(len(monkey_items)):
        nitems = len(monkey_items[i])
        for j in range(nitems):
            do_one(i)

monkey_inspections.sort()
monkey_business = monkey_inspections[-1] * monkey_inspections[-2]
print("Part 1:", monkey_business)
