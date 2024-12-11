from collections import defaultdict

import utils
from utils import deepcopy


def find_potential_loops(board):
    visited, _ = walk(board, start_pos, dir_idx)
    obstacles_to_check = set()
    loops = 0

    for locs in visited.values():

        for ny, nx in locs:

            if board[ny][nx] == "." and (ny, nx) != start_pos:
                obstacles_to_check.add((ny, nx))

    for y, x in obstacles_to_check:
        local_board = deepcopy(board)
        local_board[y][x] = "#"
        _, has_loop = walk(local_board, start_pos, dir_idx, find_loops=True)
        loops += has_loop

    return loops


def walk(board, start_pos, dir_idx, find_loops=False):
    Y, X = len(board), len(board[0])
    dy, dx = utils.DIRS[dir_idx]
    y, x = start_pos
    visited = defaultdict(set)

    while 0 <= (ny := dy + y) < Y and 0 <= (nx := dx + x) < X:

        if board[ny][nx] == "#":
            dir_idx = (dir_idx + 1) % 4
            dy, dx = utils.DIRS[dir_idx]
            continue

        if find_loops:
            if (y, x) in visited and (ny, nx) in visited[(y, x)]:
                return visited, True

        visited[(y, x)].add((ny, nx))
        y, x = ny, nx

    return visited, False


def process_puzzle_input(puzzle_input):
    board = []
    for i, row in enumerate(puzzle_input):
        board.append([])
        for j, c in enumerate(row):
            if c in (arrows := ["^", ">", "v", "<"]):
                start_pos, dir_idx = (i, j), arrows.index(c)
                board[-1].append(".")
                continue
            board[-1].append(c)

    return board, start_pos, dir_idx


if __name__ == "__main__":
    timer = utils.Timer()

    puzzle_input = utils.read_str_lines()

    # Part 1
    timer.start()
    board, start_pos, dir_idx = process_puzzle_input(puzzle_input)
    visited, _ = walk(board, start_pos, dir_idx)
    print(len(visited))
    timer.stop()  # 4.31ms

    # Part 2
    timer.start()
    board, start_pos, dir_idx = process_puzzle_input(puzzle_input)
    print(find_potential_loops(board))
    timer.stop()  # 21811.14ms
