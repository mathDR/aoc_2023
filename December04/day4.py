import numpy as np

# Part 1
with open("input.txt") as input_text:
    points = 0
    for line in input_text:
        line = line.strip("\n")
        winning_numbers = [
            int(i)
            for i in [
                c
                for c in line.split(":")[1].split("|")[0].strip().split(" ")
                if c != ""
            ]
        ]
        my_numbers = [
            int(i)
            for i in [
                c
                for c in line.split(":")[1].split("|")[1].strip().split(" ")
                if c != ""
            ]
        ]
        power = -1
        for n in my_numbers:
            if n in winning_numbers:
                power += 1
        if power > -1:
            points += 2**power
    print(points)

# Part 2
cards = dict(zip(np.arange(1, 200), np.ones(200, dtype=int)))
winners = dict(zip(np.arange(1, 200), np.zeros(200, dtype=int)))
with open("input.txt") as input_text:
    points = 0
    for line in input_text:
        line = line.strip("\n")
        line_number = int(line.split(":")[0].split("Card")[1].strip())
        winning_numbers = [
            int(i)
            for i in [
                c
                for c in line.split(":")[1].split("|")[0].strip().split(" ")
                if c != ""
            ]
        ]
        my_numbers = [
            int(i)
            for i in [
                c
                for c in line.split(":")[1].split("|")[1].strip().split(" ")
                if c != ""
            ]
        ]
        points = 0
        for n in my_numbers:
            if n in winning_numbers:
                points += 1
        winners[line_number] = points
for card in cards.keys():
    for j in range(cards[card]):
        for i in range(1, winners[card] + 1):
            cards[card + i] += 1
print(np.sum(list(cards.values())))
