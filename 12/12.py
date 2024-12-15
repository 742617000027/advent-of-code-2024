import utils


def calc_total_price(puzzle_input, sides_mode=False):
    board = process_puzzle_input(puzzle_input)
    binary_boards = make_binary_boards(board)
    return sum(sum(sum(line) for line in binary_board) * calc_multiplier(binary_board, sides_mode) for binary_board in binary_boards)


def calc_multiplier(binary_board, side_mode):
    Y, X = len(binary_board), len(binary_board[0])
    sides = 0

    for locs, dirs, boundary in [
        (
            {(y, x) for y, x in utils.product(range(Y), range(X)) if binary_board[y][x]},
            [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]][i % 2] if side_mode else [utils.DIRS[i], utils.DIRS[(i + 2) % 4]],
            utils.DIRS[i]
        )
        for i
        in range(4)
    ]:
        bdy, bdx = boundary

        while len(locs) > 0:
            queue = utils.deque([(locs.pop())])
            anything = False

            while queue:
                y, x = queue.popleft()
                by, bx = y + bdy, x + bdx

                if binary_board[by][bx] == 0:
                    anything = True
                else:
                    continue

                for dy, dx in dirs:
                    ny, nx = y + dy, x + dx

                    if 0 <= ny < Y and 0 <= nx < X and (ny, nx) in locs:
                        queue.append((ny, nx))
                        locs -= {(ny, nx)}

            sides += anything

    return sides


def make_binary_boards(board):
    Y, X = len(board), len(board[0])
    all_locations = set(utils.product(range(Y), range(X)))
    ret = []

    while len(all_locations) > 0:
        y, x = all_locations.pop()
        area_indicator = board[y][x]
        binary_board = [[0] * X for _ in range(Y)]
        binary_board[y][x] = 1
        queue = utils.deque([(y, x)])

        while queue:
            y, x = queue.popleft()

            for dy, dx in utils.DIRS:
                ny, nx = y + dy, x + dx

                if 0 <= ny < Y and 0 <= nx < X and board[ny][nx] == area_indicator and (ny, nx) in all_locations:
                    binary_board[ny][nx] = 1
                    queue.append((ny, nx))
                    all_locations -= {(ny, nx)}

        ret.append(pad(binary_board))

    return ret


def pad(binary_board):
    for line in binary_board:
        line.insert(0, 0)
        line.append(0)
    binary_board.insert(0, [0] * len(binary_board[0]))
    binary_board.append([0] * len(binary_board[0]))
    return binary_board


def find_unique_area_indicators(board):
    return set(c for line in board for c in line)


def process_puzzle_input(puzzle_input):
    return [[c for c in line] for line in puzzle_input]


if __name__ == "__main__":
    timer = utils.Timer()

    puzzle_input = utils.read_str_lines()

    # Part 1
    timer.start()
    print(calc_total_price(puzzle_input))
    timer.stop()  # 1200.55ms

    # Part 2
    timer.start()
    print(calc_total_price(puzzle_input, sides_mode=True))
    timer.stop()  # 1206.29ms
