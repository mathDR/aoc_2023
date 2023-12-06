with open("input.txt", "r") as f:
    lines = f.readlines()

star_positions = []
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "*":
            star_positions.append((x, y, char))

parts_per_star = {}
for y, line in enumerate(lines):
    num_start = 0
    num_end = 0
    number = ""
    for x, char in enumerate(line):
        if char.isnumeric():
            if number == "":
                num_start = x
            number += char
        else:
            if number != "":
                num_end = x
                symbols_surrounding = list(
                    filter(
                        lambda s: s[0] >= num_start - 1
                        and s[0] <= num_end
                        and s[1] >= y - 1
                        and s[1] <= y + 1,
                        star_positions,
                    )
                )
                if symbols_surrounding:
                    for symbol in symbols_surrounding:
                        if symbol in parts_per_star.keys():
                            parts_per_star[symbol].append(int(number))
                        else:
                            parts_per_star[symbol] = [int(number)]
            number = ""

print(sum([v[0] * v[1] for v in parts_per_star.values() if len(v) == 2]))
