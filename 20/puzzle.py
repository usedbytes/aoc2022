#!/usr/bin/env python3
import sys

items = []
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        items.append(int(line))

def transform(idx, src, amt, l):
    # If we jump more times than there are entries, then there's
    # one fewer entry in the list while we're jumping
    if abs(amt) > l:
        amt = amt % (l - 1)

    dst = (src + amt) % l

    # Account for entries shifting when wrapping
    if dst > src and amt < 0:
        dst -= 1
    if dst < src and amt > 0:
        dst += 1

    if idx > src and idx <= dst:
        return (idx - 1) % l
    if idx < src and idx >= dst:
        return (idx + 1) % l
    elif src == idx:
        return dst
    else:
        return idx

idx_now = [i for i, _ in enumerate(items)]
state = items.copy()

for i, v in enumerate(items):
    # Move the number which started at index 'i' by its value: 'v'
    #print(f'move v{v}')

    # Where is that number now?
    now_i = idx_now[i]
    #print(f'v{v} is currently at i{now_i}')

    idx_next = idx_now.copy()
    for orig_j, now_j in enumerate(idx_now):
        # Take the item that's currently at index 'now_j' and find its new
        # position, given that 'now_i' is moving by 'v'
        new_j = transform(now_j, now_i, v, len(state))

        # Store its new position
        idx_next[orig_j] = new_j

        #print(f'(v{items[orig_j]}) i{now_j} -> i{new_j}')

    # Apply it
    idx_now = idx_next

assert(len(set(idx_now)) == len(idx_now))

state = items.copy()
for i, j in enumerate(idx_now):
     state[j] = items[i]

zero_idx = items.index(0)
zero_now = idx_now[zero_idx]

print(f'zero was {zero_idx}, now {zero_now}')
a = state[(zero_now + 1000) % len(items)]
b = state[(zero_now + 2000) % len(items)]
c = state[(zero_now + 3000) % len(items)]
part1 = a + b + c
print(f'{a} + {b} + {c} = {part1}')

print("Part 1:", part1)


assert(False)

moves = []


memo = {}

for i, v in enumerate(items):
    moves.append((i, v))

def adjust(idx, moves, indent = ""):
    print(f'{indent}adjust({idx}, {moves})')
    if (idx, tuple(moves)) in memo:
        idx = memo[(idx, tuple(moves))]
        print(f'{indent}<-- memo: {idx}')
        return idx

    for i, m in enumerate(moves):
        print(f'{indent}move {m}')
        m0 = adjust(m[0], moves[:i], indent + "  ")
        print(f'{indent}m[0] {m[0]} --> {m0}')
        idx2 = transform(idx, m0, m[1], len(items))
        print(f'{indent}I was at {idx}, then idx {m0} (was {m[0]}) moved {m[1]} --> I became {idx2}')
        #print(f'{indent}transform {idx}, {m} (({m0}, {m[1]})) -> {idx2}')
        idx = idx2
    print(f'{indent}<-{idx} {moves}')
    memo[(idx, tuple(moves))] = idx
    return idx


mixed = items.copy()
for i in range(len(items)):
    print(f'top {i}')
    j = adjust(i, moves, f'{items[i]}: ') % len(items)
    mixed[j] = items[i]
    print(f'idx {i} (v {items[i]}) -> {j}')

print(mixed)
