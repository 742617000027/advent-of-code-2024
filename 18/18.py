import networkx as nx

import utils

SIDE_LEN = 71


def find_first_blocking_byte(incoming_bytes, start_at=1024):
    G = nx.grid_2d_graph(SIDE_LEN, SIDE_LEN)
    G.remove_nodes_from(incoming_bytes[:start_at])

    for node in incoming_bytes[start_at:]:
        G.remove_node(node)

        if not nx.has_path(G, (0, 0), (SIDE_LEN - 1, SIDE_LEN - 1)):
            return ",".join([str(n) for n in node])


def find_shortest_path(incoming_bytes, stop_at=1024):
    G = nx.grid_2d_graph(SIDE_LEN, SIDE_LEN)
    G.remove_nodes_from(incoming_bytes[:stop_at])
    return nx.shortest_path_length(G, (0, 0), (SIDE_LEN - 1, SIDE_LEN - 1))


def process_puzzle_input(puzzle_input):
    return [(int(x), int(y)) for x, y in [line.split(",") for line in puzzle_input]]


if __name__ == "__main__":
    timer = utils.Timer()

    puzzle_input = utils.read_str_lines()

    # Part 1
    timer.start()
    incoming_bytes = process_puzzle_input(puzzle_input)
    print(find_shortest_path(incoming_bytes))
    timer.stop()  # 13.75ms

    # Part 2
    timer.start()
    incoming_bytes = process_puzzle_input(puzzle_input)
    print(find_first_blocking_byte(incoming_bytes))
    timer.stop()  # 1839.68ms
