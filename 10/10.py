import utils


def calculate(puzzle_input, rating_mode=False):
    board = [[int(c) for c in line] for line in puzzle_input]
    paths = [[(y, x)] for y, line in enumerate(board) for x, n in enumerate(line) if n == 0]

    for elevation in range(1, 10):
        paths = [find_new_locs(board, elevation, locs) for locs in paths]

    return sum([len(locs if rating_mode else set(locs)) for locs in paths])


def find_new_locs(board, elevation, locs):
    Y, X = len(board), len(board[0])
    return [
        (ny,  nx)
        for (y, x), (dy, dx)
        in utils.product(locs, utils.DIRS)
        if 0 <= (ny := y + dy) < Y
           and 0 <= (nx := x + dx) < X
           and board[ny][nx] == elevation
    ]


if __name__ == "__main__":
    timer = utils.Timer()

    puzzle_input = utils.read_str_lines()

    # Part 1
    timer.start()
    print(calculate(puzzle_input))
    timer.stop()  # 3.77ms

    # Part 2
    timer.start()
    print(calculate(puzzle_input, rating_mode=True))
    timer.stop()  # 3.23ms
