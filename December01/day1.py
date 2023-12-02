NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def update_one(one, char):
    if one == [] and char == "o":
        return ["o"]
    if one == ["o"]:
        if char == "n":
            return ["o", "n"]
        if char == "o":
            return ["o"]
    if one == ["o", "n"] and char == "e":
        return ["o", "n", "e"]
    return []


def update_two(two, char):
    if two == [] and char == "t":
        return ["t"]
    if two == ["t"]:
        if char == "w":
            return ["t", "w"]
        if char == "t":
            return ["t"]
    if two == ["t", "w"] and char == "o":
        return ["t", "w", "o"]
    return []


def update_three(three, char):
    if three == [] and char == "t":
        return ["t"]
    if three == ["t"]:
        if char == "h":
            return ["t", "h"]
        if char == "t":
            return ["t"]
    if three == ["t", "h"] and char == "r":
        return ["t", "h", "r"]
    if three == ["t", "h", "r"] and char == "e":
        return ["t", "h", "r", "e"]
    if three == ["t", "h", "r", "e"] and char == "e":
        return ["t", "h", "r", "e", "e"]
    return []


def update_four(four, char):
    if four == [] and char == "f":
        return ["f"]
    if four == ["f"]:
        if char == "o":
            return ["f", "o"]
        if char == "f":
            return ["f"]
    if four == ["f", "o"] and char == "u":
        return ["f", "o", "u"]
    if four == ["f", "o", "u"] and char == "r":
        return ["f", "o", "u", "r"]
    return []


def update_five(five, char):
    if five == [] and char == "f":
        return ["f"]
    if five == ["f"]:
        if char == "i":
            return ["f", "i"]
        if char == "f":
            return ["f"]
    if five == ["f", "i"] and char == "v":
        return ["f", "i", "v"]
    if five == ["f", "i", "v"] and char == "e":
        return ["f", "i", "v", "e"]
    return []


def update_six(six, char):
    if six == [] and char == "s":
        return ["s"]
    if six == ["s"]:
        if char == "i":
            return ["s", "i"]
        if char == "s":
            return ["s"]
    if six == ["s", "i"] and char == "x":
        return ["s", "i", "x"]
    return []


def update_seven(seven, char):
    if seven == [] and char == "s":
        return ["s"]
    if seven == ["s"]:
        if char == "e":
            return ["s", "e"]
        if char == "s":
            return ["s"]
    if seven == ["s", "e"] and char == "v":
        return ["s", "e", "v"]
    if seven == ["s", "e", "v"] and char == "e":
        return ["s", "e", "v", "e"]
    if seven == ["s", "e", "v", "e"] and char == "n":
        return ["s", "e", "v", "e", "n"]
    return []


def update_eight(eight, char):
    if eight == [] and char == "e":
        return ["e"]
    if eight == ["e"]:
        if char == "i":
            return ["e", "i"]
        if char == "e":
            return ["e"]
    if eight == ["e", "i"] and char == "g":
        return ["e", "i", "g"]
    if eight == ["e", "i", "g"] and char == "h":
        return ["e", "i", "g", "h"]
    if eight == ["e", "i", "g", "h"] and char == "t":
        return ["e", "i", "g", "h", "t"]
    return []


def update_nine(nine, char):
    if nine == [] and char == "n":
        return ["n"]
    if nine == ["n"]:
        if char == "i":
            return ["n", "i"]
        if char == "n":
            return ["n"]
    if nine == ["n", "i"] and char == "n":
        return ["n", "i", "n"]
    if nine == ["n", "i", "n"] and char == "e":
        return ["n", "i", "n", "e"]
    return []


def check_digit(one, two, three, four, five, six, seven, eight, nine):
    if one == ["o", "n", "e"]:
        return "1"
    if two == ["t", "w", "o"]:
        return "2"
    if three == ["t", "h", "r", "e", "e"]:
        return "3"
    if four == ["f", "o", "u", "r"]:
        return "4"
    if five == ["f", "i", "v", "e"]:
        return "5"
    if six == ["s", "i", "x"]:
        return "6"
    if seven == ["s", "e", "v", "e", "n"]:
        return "7"
    if eight == ["e", "i", "g", "h", "t"]:
        return "8"
    if nine == ["n", "i", "n", "e"]:
        return "9"
    return None


with open("input.txt") as input_text:
    calibration_values = []
    calibration_sum = 0
    for line in input_text:
        start_digit = None
        end_digit = None
        one = []
        two = []
        three = []
        four = []
        five = []
        six = []
        seven = []
        eight = []
        nine = []
        for char in line:
            one = update_one(one, char)
            two = update_two(two, char)
            three = update_three(three, char)
            four = update_four(four, char)
            five = update_five(five, char)
            six = update_six(six, char)
            seven = update_seven(seven, char)
            eight = update_eight(eight, char)
            nine = update_nine(nine, char)
            digit = check_digit(one, two, three, four, five, six, seven, eight, nine)
            if digit is not None:
                if start_digit is None:
                    start_digit = digit
                if end_digit is None:
                    end_digit = digit
                else:
                    end_digit = digit

                if digit == "1":
                    one = []
                if digit == "2":
                    two = []
                if digit == "3":
                    three = []
                if digit == "4":
                    four = []
                if digit == "5":
                    five = []
                if digit == "6":
                    six = []
                if digit == "7":
                    seven = []
                if digit == "8":
                    eight = []
                if digit == "9":
                    nine = []

            if char in NUMBERS:
                if start_digit is None:
                    start_digit = char
                if end_digit is None:
                    end_digit = char
                else:
                    end_digit = char

        this_digit = int(start_digit + end_digit)
        calibration_values.append(this_digit)
        calibration_sum += this_digit
# for i, val in enumerate(calibration_values):
#     print(i + 1, val)
print(calibration_sum)
