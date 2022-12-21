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

def get_wavefront(current):
    current = sorted(current)
    max_y_x0 = 0
    for pt in current:
        if pt[0] > 0:
            break
        max_y_x0 = max(max_y_x0, pt[1])

    wf = set()
    start = (0, max_y_x0 + 1)
    to_test = [(start, True)]

    min_y = max_y_x0

    dirs = [
        (-1,  0),
        ( 0, -1),
        ( 1,  0),
        ( 0,  1),
    ]

    visited = set()
    while len(to_test) > 0:
        pt, spawn = to_test.pop()
        visited.add((pt, spawn))
        to_add = []

        new_spawn = False
        for d in dirs:
            pt2 = (pt[0] + d[0], pt[1] + d[1])

            if pt2[0] < 0 or pt2[0] > 6:
                continue

            if pt2 in current:
                wf.add(pt2)
                new_spawn = True

                min_y = min(min_y, pt2[1])
            else:
                to_add.append(pt2)

        if spawn or new_spawn:
            for pt2 in to_add:
                if (pt2, new_spawn) not in visited and (pt2, True) not in visited:
                    to_test.append((pt2, new_spawn))

    norm_wf = set()
    for pt in wf:
        norm_wf.add((pt[0], pt[1] - min_y))

    return wf, norm_wf

wavefront = set([(x, 0) for x in range(7)])
norm_wf = wavefront.copy()
states = {}
repeated = None

heights = []

max_y = 0
j = 0
i = 0
while repeated is None:
    y = max_y + 4
    x = 2

    rock_idx = i % len(rocks)
    i += 1

    settled = False
    while not settled:
        jet_idx = j % len(jets)
        j += 1

        rock = update_position(rocks[rock_idx], (x, y))

        # First knocked by jet
        jet = jets[jet_idx]
        if jet == '>':
            blocked = False
            for cell in rock:
                if cell[0] > 5 or (cell[0]+1, cell[1]) in wavefront:
                    blocked = True
            if blocked:
                pass
            else:
                x += 1
        elif jet == '<':
            blocked = False
            for cell in rock:
                if cell[0] < 1 or (cell[0]-1, cell[1]) in wavefront:
                    blocked = True
            if blocked:
                pass
            else:
                x -= 1

        rock = update_position(rocks[rock_idx], (x, y))

        # Then fall
        for cell in rock:
            if (cell[0], cell[1]-1) in wavefront:
                settled = True
                break

        if settled:
            for cell in rock:
                wavefront.add(cell)
                if cell[1] > max_y:
                    max_y = cell[1]

            wavefront, norm_wf = get_wavefront(wavefront)

            state = (rock_idx, jet_idx, tuple(sorted(norm_wf)))

            height = max([pt[1] for pt in wavefront])
            heights.append(height)

            if state in states:
                if repeated is None:
                    repeated = state
                states[state].append(i-1)
            else:
                states[state] = [i-1]
        else:
            y -= 1


def get_height_at(n):
    n_rocks = n

    repeats = states[repeated]

    height_before_cycle = heights[repeats[0]-1]
    height_of_cycle = heights[repeats[1]] - heights[repeats[0]]

    cycle_len = repeats[1] - repeats[0]
    cycle_height = height_of_cycle
    cycles = (n_rocks - repeats[0]) // cycle_len
    partial = (n_rocks - repeats[0]) % cycle_len
    partial_height = 0
    if partial > 0:
        partial_height = heights[repeats[0] + (partial - 1)] - height_before_cycle

    return height_before_cycle + (cycle_height * cycles) + partial_height

print("Part 1:", get_height_at(2022))
print("Part 2:", get_height_at(1000000000000))
