import networkx

import utils


def find_cheapest_path(maze, start, end):
    G = make_graph(maze, start)
    return networkx.shortest_path_length(G, (start, 1), (end, None), "weight")


def find_unique_tiles_on_shortest_paths(maze, start, end):
    G = make_graph(maze, start)
    return len(set([
        tile
        for path
        in networkx.all_shortest_paths(G, (start, 1), (end, None), "weight")
        for tile, _
        in path
    ]))


def make_graph(maze, start):
    ini = ((start), 1)
    G = networkx.DiGraph()
    G.add_node(ini)
    queue = utils.deque([ini])
    visited = set()

    while queue:
        u = queue.popleft()
        (y, x), dir_idx = u

        if maze[y][x] == "E":
            continue

        dy, dx = utils.DIRS[dir_idx]
        ny, nx = y + dy, x + dx
        v = ((ny, nx), None) if maze[ny][nx] == "E" else ((ny, nx), dir_idx)

        if (u, v) not in visited and maze[ny][nx] in [".", "E"]:
            G.add_edge(u, v, weight=1)
            queue.append(v)
            visited.add((u, v))

        for new_dir_idx in [(dir_idx + 1) % 4, (dir_idx - 1) % 4]:
            v = ((y, x), new_dir_idx)

            if (u, v) not in visited:
                G.add_edge(u, v, weight=1000)
                queue.append(v)
                visited.add((u, v))

    return G


def process_puzzle_input(puzzle_input):
    maze = []

    for y, line in enumerate(puzzle_input):
        maze.append([])

        for x, c in enumerate(line):

            if c == "S":
                start = (y, x)

            if c == "E":
                end = (y, x)

            maze[-1].append(c)

    return maze, start, end


if __name__ == "__main__":
    timer = utils.Timer()

    puzzle_input = utils.read_str_lines()

    # Part 1
    timer.start()
    processed = process_puzzle_input(puzzle_input)
    print(find_cheapest_path(*processed))
    timer.stop()  # 334.57ms

    # Part 2
    timer.start()
    print(find_unique_tiles_on_shortest_paths(*processed))
    timer.stop()  # 413.70ms
