from collections import defaultdict

import utils
from utils import deepcopy


def walk(board, start_pos, dir_idx, find_loops=False, reference_visits=None):
    Y, X = len(board), len(board[0])
    dy, dx = utils.DIRS[dir_idx]
    y, x = start_pos
    visited = defaultdict(set)
    loops = set()

    while 0 <= (ny := dy + y) < Y and 0 <= (nx := dx + x) < X:

        if board[ny][nx] == "#":
            dir_idx = (dir_idx + 1) % 4
            dy, dx = utils.DIRS[dir_idx]
            continue

        if find_loops and obstacle_at_new_pos_would_start_loop(board, visited, (y, x), (ny, nx), dir_idx):
            loops.add((ny, nx))

        if reference_visits is not None:
            if (y, x) in reference_visits and (ny, nx) in reference_visits[(y, x)]:
                return visited, None, True
            if (y, x) in visited and (ny, nx) in visited[(y, x)]:
                return visited, None, True

        visited[(y, x)].add((ny, nx))
        y, x = ny, nx

    visited[(y, x)].add((ny, nx))

    return visited, loops, False


def obstacle_at_new_pos_would_start_loop(board, path, pos, new_pos, dir_idx):
    modified_board = deepcopy(board)
    ny, nx = new_pos
    modified_board[ny][nx] = "#"
    _, _, would_start_loop = walk(modified_board, pos, dir_idx, reference_visits=path)
    return would_start_loop


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
    visited, _, _ = walk(board, start_pos, dir_idx, find_loops=False)
    print(len(visited))
    timer.stop()  # 4.31ms

    # Part 2
    # timer.start()
    # board, start_pos, dir_idx = process_puzzle_input(puzzle_input)
    # _, loops, _ = walk(board, start_pos, dir_idx, find_loops=True)
    # print(len(loops))
    # timer.stop()  # 15.05ms
