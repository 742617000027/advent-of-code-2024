import utils


def calculate(puzzle_input, rating_mode=False):
    board = [[int(c) for c in line] for line in puzzle_input]
    Y, X = len(board), len(board[0])
    paths = {(y, x): [(y, x)] for y, line in enumerate(board) for x, n in enumerate(line) if n == 0}

    for elevation in range(1, 10):

        for trailhead, locs in paths.items():
            new_locs = []

            for (y, x), (dy, dx) in utils.product(locs, utils.DIRS):
                ny, nx = y + dy, x + dx

                if 0 <= ny < Y and 0 <= nx < X and board[ny][nx] == elevation:
                    new_locs.append((ny, nx))

            paths[trailhead] = new_locs

    return sum([len(locs if rating_mode else set(locs)) for locs in paths.values()])


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
