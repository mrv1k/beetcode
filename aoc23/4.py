import re
import math

input1 = [
    'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
    'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
    'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
    'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
    'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
    'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11',
]
RE_DIGIT = r'\d+'

# Problem


def day4part1():
    with open('./input/4.txt', 'r') as file:
        sum = 0
        for line in file:
            numbers = line.split(': ')[1] # throw Card N: away
            elf_numbers, winning_numbers = numbers.split(' | ')
            elf_numbers = re.findall(RE_DIGIT, elf_numbers)
            winning_numbers = re.findall(RE_DIGIT, winning_numbers)
            elf_winning_numbers = list(set(elf_numbers).intersection(winning_numbers))
            if len(elf_winning_numbers):
                card_points = int(math.pow(2, len(elf_winning_numbers) - 1))
                sum += card_points
        return sum


print(day4part1())
