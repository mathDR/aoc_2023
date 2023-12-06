def parse_line_1(line):
    line = line.strip("\n")
    return [int(t) for t in line.split(":")[1].strip().split(" ") if t != ""]


def parse_data_1(times, dists):
    val = 1
    for j in range(len(dists)):
        d = dists[j]
        t = times[j]
        val *= sum([i * (t - i) > d for i in range(t + 1)])
    return val


# Part 1
with open("input.txt") as input_text:
    for line in input_text:
        if "Time" in line:
            times = parse_line_1(line)
        if "Distance" in line:
            dists = parse_line_1(line)
    print(parse_data_1(times, dists))


def parse_line_2(line):
    line = line.strip("\n")
    return int("".join([t for t in line.split(":")[1].strip().split(" ") if t != ""]))


def parse_data_2(t, d):
    return sum([i * (t - i) > d for i in range(t + 1)])


# Part 2
with open("input.txt") as input_text:
    for line in input_text:
        if "Time" in line:
            times = parse_line_2(line)
        if "Distance" in line:
            dists = parse_line_2(line)
    print(parse_data_2(times, dists))
