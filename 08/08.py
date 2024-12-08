from collections import defaultdict

import utils


def find_unique_antinodes(puzzle_input, whoops=True):
    antennas = process_puzzle_input(puzzle_input)
    limits = len(puzzle_input), len(puzzle_input[0])
    antinodes = dict()

    for antenna, locations in antennas.items():
        antinodes[antenna] = find_antinodes_for_antenna_type(locations, limits, whoops)

    return set.union(*antinodes.values())


def find_antinodes_for_antenna_type(locations, limits, whoops):
    antinodes = set()

    for pair in utils.combinations(locations, 2):
        antinodes |= find_antinodes_for_antenna_pair(pair, limits, whoops)

    if not whoops:
        antinodes |= locations

    return antinodes


def find_antinodes_for_antenna_pair(pair, limits, whoops):
    antinodes = set()
    loc1, loc2 = pair
    Y, X = limits
    loc1y, loc1x = loc1
    loc2y, loc2x = loc2
    dy, dx = vec(loc1, loc2)

    step = 1

    while True:

        added_ant1 = False
        added_ant2 = False

        if 0 <= (ant1y := loc1y - (dy * step)) < Y and 0 <= (ant1x := loc1x - (dx * step)) < X:
            antinodes.add((ant1y, ant1x))
            added_ant1 = True

        if 0 <= (ant2y := loc2y + (dy * step)) < Y and 0 <= (ant2x := loc2x + (dx * step)) < X:
            antinodes.add((ant2y, ant2x))
            added_ant2 = True

        if not (added_ant1 or added_ant2) or whoops:
            break

        step += 1

    return antinodes


def vec(loc1, loc2):
    loc1y, loc1x = loc1
    loc2y, loc2x = loc2
    return (loc2y - loc1y, loc2x - loc1x)


def process_puzzle_input(puzzle_input):
    antennas = defaultdict(set)
    for y, line in enumerate(puzzle_input):
        for x, c in enumerate(line):
            if c != ".":
                antennas[c].add((y, x))
    return antennas


if __name__ == "__main__":
    timer = utils.Timer()

    puzzle_input = utils.read_str_lines()

    # Part 1
    timer.start()
    unique_antinodes = find_unique_antinodes(puzzle_input)
    print(len(unique_antinodes))
    timer.stop()  # 0.88ms

    # Part 2
    timer.start()
    unique_antinodes = find_unique_antinodes(puzzle_input, whoops=False)
    print(len(unique_antinodes))
    timer.stop()  # 0.53ms
