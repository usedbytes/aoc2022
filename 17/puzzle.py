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

# For the record, I'm assuming that this won't scale to Part 2
occupied = {
    (0, 0): True,
    (1, 0): True,
    (2, 0): True,
    (3, 0): True,
    (4, 0): True,
    (5, 0): True,
    (6, 0): True,
}

def update_position(rock, pos):
    new_pos = []
    for cell in rock:
        new_pos.append((pos[0] + cell[0], pos[1] + cell[1]))
    return new_pos

max_y = 0
j = 0
for i in range(2022):
    y = max_y + 4
    x = 2

    settled = False
    while not settled:
        rock = update_position(rocks[i % len(rocks)], (x, y))

        # First knocked by jet
        jet = jets[j % len(jets)]
        j += 1
        if jet == '>':
            blocked = False
            for cell in rock:
                if cell[0] > 5 or (cell[0]+1, cell[1]) in occupied:
                    blocked = True
            if blocked:
                pass
            else:
                x += 1
        elif jet == '<':
            blocked = False
            for cell in rock:
                if cell[0] < 1 or (cell[0]-1, cell[1]) in occupied:
                    blocked = True
            if blocked:
                pass
            else:
                x -= 1

        rock = update_position(rocks[i % len(rocks)], (x, y))

        # Then fall
        for cell in rock:
            if (cell[0], cell[1]-1) in occupied:
                settled = True
                break

        if settled:
            for cell in rock:
                occupied[cell] = True
                if cell[1] > max_y:
                    max_y = cell[1]
        else:
            y -= 1
print("Part 1:", max_y)
