#!/usr/bin/env python3
import sys
import itertools

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
    for goal, r in rates.items():
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

#part1 = evaluate('AA', 0, 30, [])
#print("Part 1:", part1)

options = []
for valve, rate in rates.items():
    if rate != 0:
        options.append(valve)
pairs = set(list(itertools.combinations(options, 2)))
new_pairs = list(pairs.copy())
for p in pairs:
    new_pairs.append((p[1], p[0]))
pairs = new_pairs
print(pairs, len(pairs))

def double_visit(currents, score, ts, on):
    if ts[0] <= 0 or ts[1] <= 0:
        return score

    best_score = score

    for pair in pairs:
        if pair[0] in on or pair[1] in on:
            # Can't turn them on again
            continue

        if pair[0] == '':
            steps0 = 1
        else:
            steps0 = shortest_route[currents[0]][pair[0]]
        if pair[1] == '':
            steps1 = 1
        else:
            steps1 = shortest_route[currents[1]][pair[1]]

        steps = (steps0, steps1)

        new_ts = (ts[0] - (1 + steps[0]), ts[1] - (1 + steps[1]))
        if new_ts[0] < 0 or new_ts[1] < 0:
            # Unreachable, we'd run out of time before getting there
            continue

        contribs = (rates[pair[0]] * new_ts[0], rates[pair[1]] * new_ts[1])
        #if contribs[0] == 0 or contribs[1] == 0:
        #    # No point in wasting time on turning on a valve with rate 0
        #    continue

        # Assuming we turn on 'pair' next, what's the best score we can get?
        new_on = on.copy()
        if pair[0] != '':
            new_on.append(pair[0])
        if pair[1] != '':
            new_on.append(pair[1])
        new_score = double_visit(pair, score + contribs[0] + contribs[1], new_ts, new_on)
        if new_score > best_score:
            best_score = new_score

    # Return the best option.
    return best_score

#def tick(t, current_rate, score, on, my_t, my_dst, ele_t, ele_dst):
#    score += current_rate
#    if t == 0:
#        return score
#
#    best_score = score
#
#    if t == my_t:
#        new_on = on.copy()
#        if t != 26:
#            new_on.append(my_dst)
#        new_rate = current_rate + rates[my_dst]
#        print(shortest_route[my_dst])
#        for new_dst, steps in shortest_route[my_dst].items():
#            if new_dst in new_on or new_dst == ele_dst:
#                continue
#            print(t, new_rate, score, new_on, t, steps, new_dst, ele_t, ele_dst)
#            new_score = tick(t, new_rate, score, new_on, t - (steps + 1), new_dst, ele_t, ele_dst)
#            if new_score > best_score:
#                best_score = new_score
#        return best_score
#    elif t == ele_t:
#        new_on = on.copy()
#        if t != 26:
#            new_on.append(ele_dst)
#        new_rate = current_rate + rates[ele_dst]
#        for new_dst, steps in shortest_route[ele_dst].items():
#            if new_dst in new_on or new_dst == my_dst:
#                continue
#            new_score = tick(t, new_rate, score, new_on, my_t, my_dst, t - (steps + 1), new_dst)
#            if new_score > best_score:
#                best_score = new_score
#        return best_score
#    else:
#        return tick(t - 1, current_rate, score, on, my_t, my_dst, ele_t, ele_dst)

part2 = double_visit(['AA', 'AA'], 0, [26, 26], [])
#part2 = tick(26, 0, 0, [], 26, 'AA', 26, 'AA')
print("Part 2:", part2)
