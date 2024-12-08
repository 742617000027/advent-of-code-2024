import math
from operator import add, mul

import utils


def is_valid(result, terms, with_concat=False):
    if utils.reduce(add, terms, 0) == result or utils.reduce(mul, terms, 1) == result:
        return True

    for ops in utils.product([add, mul, concat] if with_concat else [add, mul], repeat=len(terms) - 1):
        a = terms[0]
        for i, op in enumerate(ops, start=1):
            b = terms[i]
            a = op(a, b)

        if a == result:
            return True

    return False


def concat(a, b):
    exponent = int(math.log10(b)) + 1
    return a * 10 ** exponent + b


def process_puzzle_input(puzzle_input):
    return [(int(line.split(": ")[0]), [int(t) for t in line.split(": ")[1].split()]) for line in puzzle_input]


if __name__ == "__main__":
    timer = utils.Timer()

    puzzle_input = utils.read_str_lines()

    # Part 1
    timer.start()
    processed = process_puzzle_input(puzzle_input)
    print(sum([result * is_valid(result, terms) for result, terms in processed]))
    timer.stop()  # 120.39ms

    # Part 2
    timer.start()
    processed = process_puzzle_input(puzzle_input)
    print(sum([result * is_valid(result, terms, with_concat=True) for result, terms in processed]))
    timer.stop()  # 10093.74ms
