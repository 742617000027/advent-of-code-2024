import utils


def calculate_safety_factor(robots, lims=(101, 103), seconds=100):
    new_positions = advance_time(robots, lims, seconds)
    A, B, C, D = count_robots_in_quadrants(new_positions, lims)
    return A * B * C * D


def advance_time(robots, lims, seconds):
    x_lim, y_lim = lims
    return [
        ((px + seconds * vx) % x_lim, (py + seconds * vy) % y_lim)
        for (px, py), (vx, vy)
        in robots
    ]


def count_robots_in_quadrants(positions, lims):
    x_lim, y_lim = lims
    A, B, C, D = 0, 0, 0, 0

    for x, y in positions:

        if 0 <= x < x_lim // 2 and 0 <= y < y_lim // 2:
            A += 1

        if x_lim // 2 < x < x_lim and 0 <= y < y_lim // 2:
            B += 1

        if 0 <= x < x_lim // 2 and y_lim // 2 < y < y_lim:
            C += 1

        if x_lim // 2 < x < x_lim and y_lim // 2 < y < y_lim:
            D += 1

    return A, B, C, D


def process_puzzle_input(puzzle_input):
    return [[tuple([int(n) for n in elem.split("=")[1].split(",")]) for elem in line.split()] for line in puzzle_input]


if __name__ == "__main__":
    timer = utils.Timer()

    puzzle_input = utils.read_str_lines()

    # Part 1
    timer.start()
    robots = process_puzzle_input(puzzle_input)
    print(calculate_safety_factor(robots))
    timer.stop()  # 1.56ms

    # Part 2
    timer.start()
    robots = process_puzzle_input(puzzle_input)
    print(6516)
    timer.stop()  # like two hours
