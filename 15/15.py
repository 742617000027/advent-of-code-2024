import utils


def calc_gps(board):
    return [100 * y + x for y, line in enumerate(board) for x, c in enumerate(line) if c == "O"]


def work(board, instructions):
    ry, rx = find_start_pos(board)
    dirs = {s: d for s, d in zip("^>v<", utils.DIRS)}

    for instruction in instructions:
        # print_board(board)
        dy, dx = dirs[instruction]
        ny, nx = ry + dy, rx + dx

        if board[ny][nx] == ".":
            board[ry][rx] = "."
            board[ny][nx] = "@"
            ry, rx = ny, nx
            continue

        if board[ny][nx] == "#":
            continue

        board, (ry, rx) = move_boxes(board, (ry, rx), (dy, dx))

    # print_board(board)
    return board


def print_board(board):
    print("\n".join(["".join(line) for line in board]))


def move_boxes(board, pos, direction):
    y, x = pos
    board[y][x] = "."
    dy, dx = direction
    boxes = []

    while True:
        y, x = y + dy, x + dx

        if board[y][x] == "#":
            y, x = pos
            board[y][x] = "@"
            return board, pos

        if board[y][x] == ".":
            y, x = y + dy, x + dx
            break

        if board[y][x] == "O":
            boxes.append((y, x))

    flip_dy, flip_dx = -dy, -dx

    for by, bx in boxes:
        board[by][bx] = "."

    for _ in boxes:
        y, x = y + flip_dy, x + flip_dx
        board[y][x] = "O"

    y, x = y + flip_dy, x + flip_dx
    board[y][x] = "@"

    return board, (y, x)


def find_start_pos(board):
    for y, line in enumerate(board):
        for x, c in enumerate(line):
            if c == "@":
                return (y, x)


def process_puzzle_input(puzzle_input):
    board, instructions = puzzle_input.split("\n\n")
    return [[c for c in line] for line in board.split("\n")], "".join(instructions.split("\n"))


if __name__ == "__main__":
    timer = utils.Timer()

    puzzle_input = utils.read()



    # Part 1
    timer.start()
    board, instructions = process_puzzle_input(puzzle_input)
    board = work(board, instructions)
    gps = calc_gps(board)
    print(sum(gps))
    timer.stop()  # 3.29ms

    # Part 2
    timer.start()
    print()
    timer.stop()  #
