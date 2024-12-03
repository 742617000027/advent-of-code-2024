import re

import utils

PATTERN = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
DO_DONT = {"do()": True, "don't()": False}


def execute_instructions(puzzle_input, cond=False):
    instructions = process_puzzle_input(puzzle_input)
    ret = []
    mult = True

    for instruction in instructions:

        if isinstance(instruction, bool):
            mult = instruction if cond else True
            continue

        if mult:
            x, y = instruction
            ret.append(x * y)

    return ret


def process_puzzle_input(puzzle_input):
    matches = re.finditer(PATTERN, puzzle_input)
    ret = []

    for elem in matches:

        if elem.groups() == (None, None):
            ret.append(DO_DONT[elem.group(0)])
        else:
            ret.append((int(elem.group(1)), int(elem.group(2))))

    return ret


if __name__ == "__main__":
    timer = utils.Timer()

    puzzle_input = utils.read()

    # Part 1
    timer.start()
    print(sum(execute_instructions(puzzle_input)))
    timer.stop()  # 1.37ms

    # Part 2
    timer.start()
    print(sum(execute_instructions(puzzle_input, cond=True)))
    timer.stop()  # 0.50m
