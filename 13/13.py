import utils


def play(claw_machines):
    tokens = 0

    for prize, a, b in claw_machines:
        zero_rem_indices = [find_zero_rem_idx(prize_val, a_val, b_val) for prize_val, a_val, b_val in zip(prize, a, b)]

        if None in zero_rem_indices:
            continue

        a_presses, b_presses = calculate_presses(prize, a, b)
        tokens += a_presses * 3 + b_presses

    return tokens


def find_zero_rem_idx(prize_val, a_val, b_val):

    for i in range(b_val):
        remaining = prize_val - i * a_val

        if remaining % b_val == 0:
            return i

    return None


def calculate_presses(prize, a, b):
    prize_x, prize_y = prize
    a_dx, a_dy = a
    b_dx, b_dy = b

    det = a_dx * b_dy - a_dy * b_dx
    a_presses = (prize_x * b_dy - prize_y * b_dx) // det
    b_presses = (prize_y * a_dx - prize_x * a_dy) // det

    if (
            a_presses * a_dx + b_presses * b_dx == prize_x
            and a_presses * a_dy + b_presses * b_dy == prize_y
            and a_presses >= 0 and b_presses >= 0
    ):
        return a_presses, b_presses

    return 0, 0


def process_puzzle_input(puzzle_input, correction=0):
    raw_claw_machines = puzzle_input.split("\n\n")
    claw_machines = []

    for raw_claw_machine in raw_claw_machines:
        a, b, prize = raw_claw_machine.split("\n")
        claw_machines.append((
            parse_coords(prize, "=", correction),
            parse_coords(a, "+"),
            parse_coords(b, "+"),
        ))

    return claw_machines


def parse_coords(text, sep, correction=0):
    _, XY = text.split(": ")
    X, Y = XY.split(", ")
    return tuple([int(val.split(sep)[1]) + correction for val in [X, Y]])


if __name__ == "__main__":
    timer = utils.Timer()

    puzzle_input = utils.read()

    # Part 1
    timer.start()
    claw_machines = process_puzzle_input(puzzle_input)
    print(play(claw_machines))
    timer.stop()  # 3.38ms

    # Part 2
    timer.start()
    claw_machines = process_puzzle_input(puzzle_input, correction=10000000000000)
    print(play(claw_machines))
    timer.stop()  # 3.01ms
