import re
import math

input1 = [
    'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',  # 4 winning
    'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',  # 2 winning
    'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',  # 2 winning
    'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',  # 1 winning
    'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
    'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11',
]
# expected 13
RE_DIGIT = r'\d+'

# figure out which of the numbers you have appear in the list of winning numbers


def day4part1():
    with open('./input/4.txt', 'r') as file:
        sum = 0
        for line in file:
            numbers = line.split(': ')[1]  # throw Card N: away
            elf_numbers, winning_numbers = numbers.split(' | ')
            elf_numbers = re.findall(RE_DIGIT, elf_numbers)
            winning_numbers = re.findall(RE_DIGIT, winning_numbers)
            elf_winning_numbers = list(
                set(elf_numbers).intersection(winning_numbers))
            print(elf_winning_numbers)
            if len(elf_winning_numbers):
                card_points = int(math.pow(2, len(elf_winning_numbers) - 1))
                sum += card_points
        return sum


# print(day4part1())

# you win copies of stratchcard below.
# eg: if 10 had 5 winnning numbers, you'd win a copy of 11 to 15

input1dup = [
    'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
    # card 1: 4 winning = copy 2 - 5

    # card 2: 1 + 1 = 2
    'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
    # card 2: 2 winning = copy 3 - 4

    # card 3: 1 + 1 + 2 = 4
    'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
    # card 3: 2 winning = copy 4 - 5

    # card 4: 1 + 1 + 2 + 4 = 8
    'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
    # card 4: 1 winning = copy 5

    # card 5: 1 + 1 + 0 + 4 + 8 = 14
    'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
    # card 5: 0 winning

    # card 6: 1 + 0 + 0 + 0 + 0 + 0
    'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11',
]
# expected 30.

# how many total scratchcards do you end up with?


def day4part2():
    # with open('./input/4.txt', 'r') as file:
    file = input1dup
    total = [1] * len(file)
    sum = 0
    for i, line in enumerate(file):
        numbers = line.split(': ')[1]  # throw Card N: away
        elf_numbers, winning_numbers = numbers.split(' | ')
        elf_numbers = re.findall(RE_DIGIT, elf_numbers)
        winning_numbers = re.findall(RE_DIGIT, winning_numbers)
        elf_winning_numbers = list(
            set(elf_numbers).intersection(winning_numbers))

    return sum


print(day4part2())
