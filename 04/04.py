import utils


def find_number_of_XMAS(puzzle_input):
    processed = process_puzzle_input(puzzle_input)
    H, W = len(processed), len(processed[0])
    count = 0

    for h in range(H):

        for w in range(W):

            # Left to right
            if (
                    w <= W - 4
                    and "".join(processed[h][w:w + 4]) == "XMAS"
            ):
                count += 1

            # Right to left
            if (
                    w >= 3
                    and "".join(processed[h][w:(w - 4 if w - 4 >= 0 else None):-1]) == "XMAS"
            ):
                count += 1

            # Top down
            if (
                    h <= H - 4
                    and processed[h][w]
                    + processed[h + 1][w]
                    + processed[h + 2][w]
                    + processed[h + 3][w]
                    == "XMAS"
            ):
                count += 1

            # Bottom up
            if (
                    h >= 3
                    and processed[h][w]
                    + processed[h - 1][w]
                    + processed[h - 2][w]
                    + processed[h - 3][w]
                    == "XMAS"
            ):
                count += 1

            # Top left to bottom right
            if (
                    w <= W - 4
                    and h <= H - 4
                    and processed[h][w]
                    + processed[h + 1][w + 1]
                    + processed[h + 2][w + 2]
                    + processed[h + 3][w + 3]
                    == "XMAS"
            ):
                count += 1

            # Top right to bottom left
            if (
                    w >= 3
                    and h <= H - 4
                    and processed[h][w]
                    + processed[h + 1][w - 1]
                    + processed[h + 2][w - 2]
                    + processed[h + 3][w - 3]
                    == "XMAS"
            ):
                count += 1

            # Bottom left to top right
            if (
                    w <= W - 4
                    and h >= 3
                    and processed[h][w]
                    + processed[h - 1][w + 1]
                    + processed[h - 2][w + 2]
                    + processed[h - 3][w + 3]
                    == "XMAS"
            ):
                count += 1

            # Bottom right to top left
            if (
                    w >= 3
                    and h >= 3
                    and processed[h][w]
                    + processed[h - 1][w - 1]
                    + processed[h - 2][w - 2]
                    + processed[h - 3][w - 3]
                    == "XMAS"
            ):
                count += 1

    return count


def find_number_of_X_MAS(puzzle_input):
    processed = process_puzzle_input(puzzle_input)
    H, W = len(processed), len(processed[0])
    count = 0

    for h in range(H - 2):

        for w in range(W - 2):

            tl_br = False
            tr_bl = False
            bl_tr = False
            br_tl = False

            # Top left to bottom right
            if (
                processed[h][w]
                + processed[h + 1][w + 1]
                + processed[h + 2][w + 2]
                == "MAS"
            ):
                tl_br = True

            # Top right to bottom left
            if (
                processed[h][w + 2]
                + processed[h + 1][w + 1]
                + processed[h + 2][w]
                == "MAS"
            ):
                tr_bl = True

            # Bottom left to top right
            if (
                processed[h + 2][w]
                + processed[h + 1][w + 1]
                + processed[h][w + 2]
                == "MAS"
            ):
                bl_tr = True

            # Bottom right to top left
            if (
                processed[h + 2][w + 2]
                + processed[h + 1][w + 1]
                + processed[h][w]
                == "MAS"
            ):
                br_tl = True

            if (
                    tl_br and (tr_bl or bl_tr)
            ) or (
                    br_tl and (tr_bl or bl_tr)
            ):
                count += 1

    return count


def process_puzzle_input(puzzle_input):
    return [[c for c in line] for line in puzzle_input]


if __name__ == "__main__":
    timer = utils.Timer()

    puzzle_input = utils.read_str_lines()

    # Part 1
    timer.start()
    print(find_number_of_XMAS(puzzle_input))
    timer.stop()  # 24.91ms

    # Part 2
    timer.start()
    print(find_number_of_X_MAS(puzzle_input))
    timer.stop()  # 9.37ms
