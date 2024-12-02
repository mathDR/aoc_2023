import os
from collections import deque


def get_input(name="input.txt"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, "r") as file:
        input_file = file.read().strip().split("\n")

    return input_file


def get_type(pos):
    if not in_bounds(pos):
        return "."
    return input_file[pos[1]][pos[0]]


def add_tup(tup1, tup2):
    return (tup1[0] + tup2[0], tup1[1] + tup2[1])


def initialise_queue(check_queue, start_pos):
    if get_type(add_tup(start_pos, (-2, 0))) in {"-", "F", "L"}:
        check_queue.append(add_tup(start_pos, (-1, 0)))

    if get_type(add_tup(start_pos, (2, 0))) in {"-", "J", "7"}:
        check_queue.append(add_tup(start_pos, (1, 0)))

    if get_type(add_tup(start_pos, (0, -2))) in {"|", "F", "7"}:
        check_queue.append(add_tup(start_pos, (0, -1)))

    if get_type(add_tup(start_pos, (0, 2))) in {"|", "J", "L"}:
        check_queue.append(add_tup(start_pos, (0, 1)))


def expand_grid(grid):
    new_grid = [
        [" " for _ in range(2 * len(grid[0]) - 1)] for _ in range(2 * len(grid) - 1)
    ]
    for j, line in enumerate(new_grid):
        for i, char in enumerate(line):
            if i % 2 == 0 and j % 2 == 0:
                new_grid[j][i] = grid[j // 2][i // 2]
            elif i % 2 == 0 and j % 2 != 0:
                new_grid[j][i] = "I"
            elif i % 2 != 0 and j % 2 == 0:
                new_grid[j][i] = "="
    return new_grid


def in_bounds(pos):
    return not (pos[0] < 0 or pos[0] >= x_len or pos[1] < 0 or pos[1] >= y_len)


def get_fill(start_pos, distance_dict, start_dir):
    initial_check = add_tup(start_pos, start_dir)
    check_queue = deque([initial_check])
    checked_set = {initial_check}
    quantity = 0

    while len(check_queue) > 0:
        current_pos = check_queue.popleft()
        current_type = get_type(current_pos)
        if current_type in {".", "-", "|", "J", "L", "F", "7"}:
            quantity += 1

        for diff in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_pos = add_tup(current_pos, diff)
            if new_pos in checked_set or new_pos in distance_dict:
                continue
            if not in_bounds(new_pos):
                return -1

            check_queue.append(new_pos)
            checked_set.add(new_pos)
    return quantity


def main():
    global input_file, x_len, y_len
    input_file = expand_grid(get_input())

    x_len = len(input_file[0])
    y_len = len(input_file)

    start_pos = (-1, -1)
    for j, line in enumerate(input_file):
        for i, char in enumerate(line):
            if char == "S":
                start_pos = (i, j)

    check_positions = {
        "F": [(1, 0), (0, 1)],
        "7": [(-1, 0), (0, 1)],
        "J": [(-1, 0), (0, -1)],
        "L": [(1, 0), (0, -1)],
        "-": [(-1, 0), (1, 0)],
        "|": [(0, -1), (0, 1)],
        "=": [(-1, 0), (1, 0)],
        "I": [(0, -1), (0, 1)],
        ".": [],
        " ": [],
    }

    check_queue = deque([])
    initialise_queue(check_queue, start_pos)
    distance_dict = {pos: 1 for pos in check_queue}
    distance_dict[start_pos] = 0
    max_distance = 0

    while len(check_queue) > 0:
        current_pos = check_queue.popleft()
        current_type = get_type(current_pos)
        for diff in check_positions[current_type]:
            new_pos = add_tup(current_pos, diff)
            if new_pos in distance_dict:
                continue

            distance_dict[new_pos] = distance_dict[current_pos] + 1
            max_distance = max(max_distance, distance_dict[new_pos])

            check_queue.append(new_pos)

    for start_dir in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        quantity = get_fill(start_pos, distance_dict, start_dir)
        if quantity > 0:
            print(quantity)
            break


if __name__ == "__main__":
    main()
