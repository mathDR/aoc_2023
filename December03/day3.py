NOT_SYMBOL = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
NUMBERS = NOT_SYMBOL[:-1]


def find_symbols_in_line(line):
    return [i for i, c in enumerate(line) if c not in NOT_SYMBOL]


def check_left(s, line):
    num = [line[s - 1]]
    line[s - 1] = "."
    z = s - 2
    flag = True
    while flag:
        if z >= 0:
            if line[z] in NUMBERS:
                num.append(line[z])
                line[z] = "."
                z -= 1
            else:
                flag = False
        else:
            flag = False
    this_val = int("".join(num[::-1]))
    return this_val, line


def check_right(s, line):
    num = [line[s + 1]]
    line[s + 1] = "."
    z = s + 2
    flag = True
    while flag:
        if z < len(line):
            if line[z] in NUMBERS:
                num.append(line[z])
                line[z] = "."
                z += 1
            else:
                flag = False
        else:
            flag = False
    this_val = int("".join(num))
    return this_val, line


def parse_line(sym, prev_sym, str_line):
    val = 0
    for c in prev_sym:
        if (str_line[c]) in NUMBERS:
            # There is an adjacent number above this symbol
            v, str_line = check_center(c, str_line)
            val += v
        if c > 0 and str_line[c - 1] in NUMBERS:
            # There is an adjacent number to the left of this symbol
            v, str_line = check_left(c, str_line)
            val += v
        if c < len(str_line) - 1 and str_line[c + 1] in NUMBERS:
            # There is an adjacent number to the right of this symbol
            v, str_line = check_right(c, str_line)
            val += v
    for c in sym:
        if c > 0 and str_line[c - 1] in NUMBERS:
            # There is an adjacent number to the left of this symbol
            v, str_line = check_left(c, str_line)
            val += v
        if c < len(str_line) - 1 and str_line[c + 1] in NUMBERS:
            # There is an adjacent number to the right of this symbol
            v, str_line = check_right(c, str_line)
            val += v
    return val, str_line


def check_center(s, line):
    num = [line[s]]
    line[s] = "."
    z = s - 1
    flag = True
    while flag:
        if z >= 0:
            if line[z] in NUMBERS:
                num.append(line[z])
                line[z] = "."
                z -= 1
            else:
                flag = False
        else:
            flag = False
    num = num[::-1]
    z = s + 1
    flag = True
    while flag:
        if z < len(line):
            if line[z] in NUMBERS:
                num.append(line[z])
                line[z] = "."
                z += 1
            else:
                flag = False
        else:
            flag = False
    this_val = int("".join(num))
    return this_val, line


def parse_line_above(sym, str_line):
    val = 0
    for c in sym:
        if (str_line[c]) in NUMBERS:
            # There is an adjacent number above this symbol
            v, str_line = check_center(c, str_line)
            val += v
        if (c > 0 and str_line[c - 1]) in NUMBERS:
            # There is an adjacent number to the upper left of this symbol
            v, str_line = check_left(c, str_line)
            val += v
        if c < len(str_line) - 1 and str_line[c + 1] in NUMBERS:
            # There is an adjacent number to the upper right of this symbol
            v, str_line = check_right(c, str_line)
            val += v
    return val


# Part 1
val = 0
with open("input.txt") as input_text:
    line_above = None
    prev_sym = None
    for line in input_text:
        line = line.strip("\n")
        sym = find_symbols_in_line(line)
        str_line = [c for c in line]
        if sym == [] and (prev_sym is None or prev_sym == []):
            line_above = str_line
            prev_sym = []
            continue
        v, str_line = parse_line(sym, prev_sym, str_line)
        val += v
        if line_above is not None:
            val += parse_line_above(sym, line_above)
        line_above = str_line
        prev_sym = sym
print(val)

# Part 2
val = 0
with open("input.txt") as input_text:
    line_above = None
    this_line = None
    next_line = None

    sym_above = None
    this_sym = None
    next_sym = None
    for line in input_text:
        line = line.strip("\n")
        next_sym = find_symbols_in_line(line)
        next_line = [c for c in line]
        val += parse_line_2(
            line_above, this_line, next_line, sym_above, this_sym, next_sym
        )
        line_above = this_line
        this_line = next_line
        sym_above = this_sym
        this_sym = next_sym

print(val)
