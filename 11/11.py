import math

import utils


def perform_blinks(number_of_blinks):
    stones = process_puzzle_input(puzzle_input)
    ledger = dict()
    total = 0

    for stone in stones:
        total += handle_stones(stone, number_of_blinks, ledger)

    return total


def handle_stones(stone, blink, ledger):
    if (stone, blink) in ledger:
        return ledger[(stone, blink)]

    if blink == 0:
        ret = 1

    elif stone == 0:
        ret = handle_stones(1, blink - 1, ledger)

    elif (n_digits := get_number_of_digits(stone)) % 2 == 0:
        left, right = split_stones(stone, n_digits)
        ret = handle_stones(left, blink - 1, ledger) + handle_stones(right, blink - 1, ledger)

    else:
        ret = handle_stones(stone * 2024, blink - 1, ledger)

    ledger[(stone, blink)] = ret
    return ret


def split_stones(stone, n_digits):
    return divmod(stone, 10 ** (n_digits // 2))


def get_number_of_digits(n):
    return int(math.log10(n)) + 1


def process_puzzle_input(puzzle_input):
    return [int(n) for n in puzzle_input.split()]


if __name__ == "__main__":
    timer = utils.Timer()

    puzzle_input = utils.read()

    # Part 1
    timer.start()
    print(perform_blinks(25))
    timer.stop()  # 2.74ms

    # Part 2
    timer.start()
    print(perform_blinks(75))
    timer.stop()  # 68.87ms
