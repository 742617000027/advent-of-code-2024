import utils


def get_total_safety(puzzle_input, dampener=False):
    processed = process_puzzle_input(puzzle_input)
    return sum([get_single_safety(report, dampener) for report in processed])


def get_single_safety(report, dampener):
    for i in range(len(report)):
        d = diff(report[:i] + report[i + dampener:])
        gt0 = []
        lt0 = []
        within_interval = []

        for n in d:
            gt0.append(n > 0)
            lt0.append(n < 0)
            within_interval.append(1 <= abs(n) <= 3)

        cond = (all(gt0) or all(lt0)) and all(within_interval)

        if cond:
            return True

        if not dampener and not cond:
            return False

    return False


def process_puzzle_input(puzzle_input):
    return [[int(n) for n in line.split()] for line in puzzle_input]


def diff(l):
    ret = []
    for i in range(1, len(l)):
        ret.append(l[i] - l[i - 1])
    return ret


if __name__ == "__main__":
    timer = utils.Timer()

    puzzle_input = utils.read_str_lines()

    # Part 1
    timer.start()
    print(get_total_safety(puzzle_input))
    timer.stop()  # 2.72ms

    # Part 2
    timer.start()
    print(get_total_safety(puzzle_input, dampener=True))
    timer.stop()  # 5.23ms
