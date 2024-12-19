import utils


def play(claw_machines):
    tokens = 0

    for prize, a, b in claw_machines:
        zero_rem_indices = find_zero_rem_indices(prize, a, b)

        if None in zero_rem_indices:
            continue

        a_presses, b_presses = calculate_presses(prize, a, b, zero_rem_indices)
        tokens += a_presses * 3 + b_presses

    return tokens


def find_zero_rem_indices(prize, a, b):
    prize_x, prize_y = prize
    a_dx, a_dy = a
    b_dx, b_dy = b

    x_remainders, y_remainders = set(), set()
    x_zero_rem_idx, y_zero_rem_idx = None, None
    x_done, y_done = False, False

    for a_presses, (x_distance, y_distance) in enumerate(zip(range(prize_x, 0, -a_dx), range(prize_y, 0, -a_dy))):

        if not x_done:
            x_remainders, x_zero_rem_idx, x_done = update_rems(
                x_distance,
                b_dx,
                x_remainders,
                x_zero_rem_idx,
                x_done,
                a_presses
            )

        if not y_done:
            y_remainders, y_zero_rem_idx, y_done = update_rems(
                y_distance,
                b_dy,
                y_remainders,
                y_zero_rem_idx,
                y_done,
                a_presses
            )

        if x_done and y_done:
            break

    return x_zero_rem_idx, y_zero_rem_idx


def update_rems(distance, bd, rems, zero_rem, done, a_presses):
    rem = distance % bd

    if rem in rems and 0 not in rems:
        return rems, None, True

    rems.add(rem)

    if rem == 0:
        done = True
        zero_rem = a_presses

    return rems, zero_rem, done


def calculate_presses(prize, a, b, zero_rem_indices):
    price_x, price_y = prize
    a_dx, a_dy = a
    b_dx, b_dy = b
    x_zero_rem_idx, y_zero_rem_idx = zero_rem_indices

    p1x, p1y = x_zero_rem_idx, (price_x - x_zero_rem_idx * a_dx) // b_dx
    p2x, p2y = y_zero_rem_idx, (price_y - y_zero_rem_idx * a_dy) // b_dy
    m1, m2 = -a_dx / b_dx, -a_dy / b_dy

    a_presses = round((m1 * p1x - m2 * p2x + ((price_y - p2x * a_dy) // b_dy) - p1y) / (m1 - m2))
    b_presses = round(m1 * a_presses - m1 * x_zero_rem_idx + p1y)

    if not (
            price_x - (a_presses * a_dx + b_presses * b_dx) == 0
            and price_y - (a_presses * a_dy + b_presses * b_dy) == 0
    ):
        return 0, 0

    return a_presses, b_presses


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
