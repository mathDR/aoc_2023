BOUNDS = [14, 12, 13]


def analyze(tr):
    blue = 0
    red = 0
    green = 0
    for tr in game.split(","):
        if "blue" in tr:
            blue = int(tr.split("blue")[0].strip(" "))
        if "red" in tr:
            red = int(tr.split("red")[0].strip(" "))
        if "green" in tr:
            green = int(tr.split("green")[0].strip(" "))
    return blue, red, green


# Part 1
id_sum = 0
with open("input.txt") as input_text:
    for line in input_text:
        game_number = int(line.split(":")[0].split(" ")[-1])
        games = line.strip("\n").split(":")[1].split(";")
        possible = True
        for game in games:
            ag = analyze(game)
            for i in range(3):
                if ag[i] > BOUNDS[i]:
                    possible = False
            if not possible:
                break
        if possible:
            id_sum += game_number
    print(id_sum)

# Part 2
power_sum = 0
with open("input.txt") as input_text:
    for line in input_text:
        game_number = int(line.split(":")[0].split(" ")[-1])
        games = line.strip("\n").split(":")[1].split(";")
        mb = 0
        mr = 0
        mg = 0
        for game in games:
            blue, red, green = analyze(game)
            if blue > mb:
                mb = blue
            if red > mr:
                mr = red
            if green > mg:
                mg = green
        power_sum += mb * mr * mg
    print(power_sum)
