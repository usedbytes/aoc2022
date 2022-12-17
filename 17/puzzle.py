#!/usr/bin/env python3
import sys

rocks = [
    [
        (0, 0), (1, 0), (2, 0), (3, 0),
    ],
    [
        (0, 1), (1, 0), (1, 1), (1, 2), (2, 1),
    ],
    [
        (0, 0), (1, 0), (2, 0), (2, 1), (2, 2),
    ],
    [
        (0, 0), (0, 1), (0, 2), (0, 3),
    ],
    [
        (0, 0), (1, 0), (0, 1), (1, 1),
    ],
]

with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        jets = line


rock_idx = 0
jet_idx = 0

floor = [0] * 7

j = 0
for i in range(2022):
    y = max(floor) + 4
    x = 2
    rock = rocks[i % len(rocks)] 

    print("Rock", i)
    settled = False
    while not settled:
        # First knocked by jet
        jet = jets[j % len(jets)]
        j += 1
        if jet == '>':
            blocked = False
            for cell in rock:
                pos = (x + cell[0], y + cell[1])
                if pos[0] > 5 or floor[pos[0]+1] >= pos[1]:
                    blocked = True
            if blocked:
                print("right blocked")
                pass
            else:
                print("right ok")
                x += 1
        elif jet == '<':
            blocked = False
            for cell in rock:
                pos = (x + cell[0], y + cell[1])
                if pos[0] < 1 or floor[pos[0]-1] >= pos[1]:
                    blocked = True
            if blocked:
                print("left blocked")
                pass
            else:
                print("left ok")
                x -= 1

        # Then fall
        for cell in rock:
            pos = (x + cell[0], y + cell[1])
            print(floor, pos)
            if floor[pos[0]] == (pos[1] - 1):
                settled = True
                break

        if settled:
            #print("fall blocked")
            for cell in rock:
                pos = (x + cell[0], y + cell[1])
                floor[pos[0]] = max(floor[pos[0]], pos[1])
        else:
            y -= 1
            #print("fall ok")
    print("settled", floor)
print("Part 1:", max(floor))
