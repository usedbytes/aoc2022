#!/usr/bin/env python3
import sys

vals = {}
exprs = {}

part2 = len(sys.argv) > 2

with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()

        parts = line.split()
        name = parts[0].strip(':')

        if part2 and (name == "humn"):
            continue
        elif part2 and (name == "root"):
            exprs[name] = (parts[1], '=', parts[3])
        elif len(parts) == 2:
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

    if len(to_delete) == 0:
        break

if not part2:
    print("Part 1:", vals['root'])
    exit()

# Now exprs contains everything which depends on humn.

def expand(name):
    val = vals.get(name)
    if val is not None:
        return val

    expr = exprs.get(name)
    if not expr:
        return (name)

    a = expr[0]
    if a in vals:
        a = vals[a]
    else:
        a = expand(a)

    b = expr[2]
    if b in vals:
        b = vals[b]
    else:
        b = expand(b)

    return (a, expr[1], b)

def pretty_print(expr):
    if isinstance(expr, int):
        return str(expr)
    elif isinstance(expr, str):
        return expr

    return f'({pretty_print(expr[0])} {pretty_print(expr[1])} {pretty_print(expr[2])})'

root_expr = exprs['root']
left = pretty_print(expand(root_expr[0]))
right = pretty_print(expand(root_expr[2]))

print(f'{left} == {right}')

# Last year I wrote my own symbolic parser/solver... this year, I'm lazy
import sympy
from sympy.solvers.diophantine.diophantine import diop_solve

left_sym = sympy.parse_expr(left)
right_sym = sympy.parse_expr(right)

ans = int(sympy.solvers.solvers.nsolve(left_sym - right_sym, 1))

print("Part 2:", ans)
