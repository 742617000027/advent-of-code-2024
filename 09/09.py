import utils


def defragment(files, free):
    defragmented = [files.pop(0)]

    for file_id, file_start, file_len in files[::-1]:
        moved = False

        for i, (free_start, free_len) in enumerate(free):

            if free_start > file_start:
                break

            remaining = free_len - file_len

            if remaining >= 0:
                moved = True
                defragmented.append((file_id, free_start, file_len))
                break

        if not moved:
            defragmented.append((file_id, file_start, file_len))

        if remaining > 0:
            free[i] = (free_start + file_len, remaining)

        if remaining == 0:
            free = free[:i] + free[i + 1:]

    return defragmented


def fragment(files, free):
    fragmented = []
    file_id, _, file_len = files.pop()

    for free_start, free_len in free:

        if not files and file_len > 0:
            last_element_id, last_element_start_idx, last_element_length = fragmented[-1]
            fragmented[-1] = (last_element_id, last_element_start_idx, last_element_length + file_len)
            break

        if files:
            fragmented.append(files.pop(0))

        while free_len > 0:

            if file_len == 0:
                file_id, _, file_len = files.pop()

            blocks_to_move = min(file_len, free_len)
            fragmented.append((file_id, free_start, blocks_to_move))

            file_len -= blocks_to_move
            free_len -= blocks_to_move
            free_start += blocks_to_move

    return fragmented


def checksum(elements):
    total = 0
    for element_id, start, length in elements:
        total += element_id * (length * (2 * start + length - 1) // 2)
    return total


def process_puzzle_input(puzzle_input):
    files = []
    free = []
    start = 0

    for i, elem in enumerate(puzzle_input):
        length = int(elem)
        if i % 2 == 0:

            files.append((i // 2, start, length))
        else:
            free.append((start, length))
        start += length

    return files, free


if __name__ == "__main__":
    timer = utils.Timer()

    puzzle_input = utils.read()

    # Part 1
    timer.start()
    files, free = process_puzzle_input(puzzle_input)
    fragmented = fragment(files, free)
    print(checksum(fragmented))
    timer.stop()  #  13.89ms

    # Part 2
    timer.start()
    files, free = process_puzzle_input(puzzle_input)
    defragmented = defragment(files, free)
    print(checksum(defragmented))
    timer.stop()  # 334.64ms
