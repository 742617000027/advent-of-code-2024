from collections import defaultdict

import utils


def find_middle_pages_of_correctly_ordered_updates(puzzle_input):
    rules, updates = process_puzzle_input(puzzle_input)
    return [update[len(update) // 2] for update in updates if is_correctly_ordered(update, rules)]


def find_middle_pages_of_incorrectly_but_then_fixed_updates(puzzle_input):
    rules, updates = process_puzzle_input(puzzle_input)
    reverse_rules = defaultdict(list)
    [reverse_rules[after].append(before) for before, afters in rules.items() for after in afters]
    return [fix_update(update, rules, reverse_rules)[len(update) // 2] for update in updates if
            not is_correctly_ordered(update, rules)]


def is_correctly_ordered(update, rules):
    return all([i < update.index(after) for i, n in enumerate(update) for after in rules[n] if after in update])


def fix_update(update, rules, reverse_rules):
    fixed = []

    for before, afters in [(b, a) for b, a in rules.items() if b in update]:
        lower_bound = max([fixed.index(b) for b in reverse_rules[before] if b in fixed] or [-1]) + 1
        upper_bound = min([len(fixed)] + [fixed.index(after) for after in [a for a in afters if a in fixed]])
        fixed.insert(max(lower_bound, upper_bound), before)

    return fixed


def process_puzzle_input(puzzle_input):
    rules_block, updates_block = puzzle_input.split("\n\n")
    rules = defaultdict(list)
    [rules[before].append(after) for before, after in
     ([int(x) for x in line.split("|")] for line in rules_block.split("\n"))]
    updates = [[int(x) for x in line.split(",")] for line in updates_block.split("\n")]

    return rules, updates


if __name__ == "__main__":
    timer = utils.Timer()

    puzzle_input = utils.read()

    # Part 1
    timer.start()
    print(sum(find_middle_pages_of_correctly_ordered_updates(puzzle_input)))
    timer.stop()  # 9.94ms

    # Part 2
    timer.start()
    print(sum(find_middle_pages_of_incorrectly_but_then_fixed_updates(puzzle_input)))
    timer.stop()  # 15.05ms
