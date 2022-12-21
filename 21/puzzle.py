#!/usr/bin/env python3
import sys

vals = {}
exprs = {}

with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()

        parts = line.split()
        name = parts[0].strip(':')

        if len(parts) == 2:
            vals[name] = int(parts[1])
        else:
            exprs[name] = (parts[1], parts[2], parts[3])

while len(exprs):
    to_delete = []
    for name, expr in exprs.items():
        a = vals.get(expr[0])
        op = expr[1]
        b = vals.get(expr[2])

        if a and b:
            if op == '+':
                v = a + b
            elif op == '-':
                v = a - b
            elif op == '*':
                v = a * b
            elif op == '/':
                v = a // b
            vals[name] = v
            to_delete.append(name)
    for name in to_delete:
        del exprs[name]

print("Part 1:", vals['root'])
