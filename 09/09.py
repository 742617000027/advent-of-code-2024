import utils


def defragment(files, free):
    defragmented = checksum(files.pop(0))

    for file_id, file_start, file_len in files[::-1]:

        for i, (free_start, free_len) in enumerate(free):

            if free_start > file_start:
                defragmented += checksum((file_id, file_start, file_len))
                break

            remaining = free_len - file_len

            if remaining >= 0:
                defragmented += checksum((file_id, free_start, file_len))

                if remaining > 0:
                    free[i] = (free_start + file_len, remaining)

                else:
                    free = free[:i] + free[i + 1:]

                break

        else:
            defragmented += checksum((file_id, file_start, file_len))

    return defragmented


def fragment(files, free):
    fragmented = 0
    file_id, file_start, file_len = files.pop()

    for free_start, free_len in free:

        if not files and file_len > 0:
            fragmented += checksum((file_id, file_start, file_len))
            break

        if files:
            fragmented += checksum(files.pop(0))

        while free_len > 0:

            if file_len == 0:
                file_id, file_start, file_len = files.pop()

            blocks_to_move = min(file_len, free_len)
            fragmented += checksum((file_id, free_start, blocks_to_move))

            file_len -= blocks_to_move
            free_len -= blocks_to_move
            free_start += blocks_to_move

    return fragmented


def checksum(element):
    element_id, start, length = element
    return element_id * (length * (2 * start + length - 1) // 2)


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
    print(fragment(files, free))
    timer.stop()  # 11.33ms

    # Part 2
    timer.start()
    files, free = process_puzzle_input(puzzle_input)
    print(defragment(files, free))
    timer.stop()  # 341.92ms
