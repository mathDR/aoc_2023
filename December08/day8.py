import math


def parse_moves_line(line):
    line = line.strip("\n")
    return [m for m in line]


def update_nodes(line):
    line = line.strip("\n")
    key = line.split("=")[0].strip()
    z = line.split("=")[1].strip()
    L_val = z.split(",")[0].strip("(")
    R_val = z.split(",")[1].strip().strip(")")
    return {key: {"L": L_val, "R": R_val}}


def count_moves(moves, nodes):
    val = "AAA"
    move_index = 0
    total_count = 0
    while val != "ZZZ":
        move = moves[move_index]
        if move_index == len(moves) - 1:
            move_index = 0
        else:
            move_index += 1
        val = nodes[val][move]
        total_count += 1
    return total_count


# Part 1
with open("input.txt") as input_text:
    moves_flag = True
    nodes = {}
    for line in input_text:
        if moves_flag:
            moves_flag = False
            moves = parse_moves_line(line)
        elif line == "\n":
            continue
        else:
            dd = update_nodes(line)
            nodes.update(dd)
    print(count_moves(moves, nodes))


def update_nodes_2(line):
    line = line.strip("\n")
    key = line.split("=")[0].strip()
    z = line.split("=")[1].strip()
    L_val = z.split(",")[0].strip("(")
    R_val = z.split(",")[1].strip().strip(")")
    if key[2] == "A":
        sn = key
    else:
        sn = None
    return sn, {key: {"L": L_val, "R": R_val}}


def count_moves_2(moves, nodes, starting_nodes):
    def count_moves(moves, nodes, starting_val):
        val = starting_val
        move_index = 0
        total_count = 0
        while val[2] != "Z":
            move = moves[move_index]
            if move_index == len(moves) - 1:
                move_index = 0
            else:
                move_index += 1
            val = nodes[val][move]
            total_count += 1
        return total_count

    states = starting_nodes.copy()
    counts = [0] * len(states)
    for i, state in enumerate(states):
        counts[i] = count_moves(moves, nodes, state)
    return counts


# Part 2
with open("input.txt") as input_text:
    moves_flag = True
    nodes = {}
    starting_nodes = []
    for line in input_text:
        if moves_flag:
            moves_flag = False
            moves = parse_moves_line(line)
        elif line == "\n":
            continue
        else:
            sn, dd = update_nodes_2(line)
            if sn is not None:
                starting_nodes.append(sn)
            nodes.update(dd)
    print(math.lcm(*count_moves_2(moves, nodes, starting_nodes)))
