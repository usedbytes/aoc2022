#!/usr/bin/env python3
import sys

rates = {}
links = {}

# Parse network
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        parts = line.split()
        valve = parts[1]
        rate = int(parts[4][5:].strip(';'))
        link = [p.strip(',') for p in parts[9:]]

        rates[valve] = rate
        links[valve] = link

shortest_route = { }

# Returns the shortest route from 'current' to 'goal', having already
# visited everything in 'path'
def route_to(current, goal, path):
    if current == goal:
        return len(path)

    min_len = len(rates)
    for next_valve in links[current]:
        if next_valve in path:
            # No loops
            continue

        new_path = path.copy()
        new_path.append(current)
        min_len = min(min_len, route_to(next_valve, goal, new_path))
    return min_len

# Populate a dictionary of dictionaries storing the shortest routes
# between nodes.
# Note: This doubles every single link. Could do better.
for start in rates:
    shortest_route[start] = {}
    for goal in rates:
        shortest_route[start][goal] = route_to(start, goal, [])

# Recursively, given you are at valve 'current', with 't' minutes remaining,
# with the valves in 'on' having contributed total pressure relief of 'score'
# so far, return the best achievable score?
def evaluate(current, score, t, on):
    if t <= 0:
        # Time's up.
        return score

    # There's always the option of never moving again, which would give
    # no change in score.
    best_score = score
    new_t = 0

    # Go through each not-already-on valve, and determine how much it
    # could contribute to score if you visited it next (recursively)
    for v, steps in shortest_route[current].items():
        if v in on:
            # Can't turn it on again, so not an option
            continue

        # Visiting valve 'v' and turning it on would leave 'new_t' minutes
        # remaining
        new_t = (t - (1 + steps))
        if new_t < 0:
            # Unreachable, we'd run out of time before getting there
            continue

        # Turning on valve 'v' would add 'contrib' to the total score
        contrib = rates[v] * new_t
        if contrib == 0:
            # No point in wasting time on turning on a valve with rate 0
            continue

        # Assuming we turn on 'v' next, what's the best score we can get?
        new_on = on.copy()
        new_on.append(v)
        new_score = evaluate(v, score + contrib, new_t, new_on)
        if new_score > best_score:
            best_score = new_score

    # Return the best option.
    return best_score

part1 = evaluate('AA', 0, 30, [])
print("Part 1:", part1)
