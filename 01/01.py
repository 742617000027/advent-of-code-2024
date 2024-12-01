import utils


def get_distances(puzzle_input):
    a, b = process_puzzle_input(puzzle_input)
    return [abs(x - y) for x, y in zip(sorted(a), sorted(b))]


def get_similarities(puzzle_input):
    a, b = process_puzzle_input(puzzle_input)
    counts = {n: b.count(n) for n in set(a)}
    return [n * counts[n] for n in a]


def process_puzzle_input(puzzle_input):
    a, b = zip(*[[int(n) for n in line.split()] for line in puzzle_input])
    return a, b


if __name__ == "__main__":
    timer = utils.Timer()

    puzzle_input = utils.read_str_lines()

    # Part 1
    timer.start()
    print(sum(get_distances(puzzle_input)))
    timer.stop()  # 1.33ms

    # Part 2
    timer.start()
    print(sum(get_similarities(puzzle_input)))
    timer.stop()  # 6.40ms