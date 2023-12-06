import re
input1 = [  # #      ∅∅∅∅∅
    '467..114..',  # .114. -> {114} is not adjacent to any symbols
    # '46..114...',  # .114. -> {114} is not adjacent to any symbols
    '...*......',  # .....
    '..35..633.',
    '......#...',
    # '..111....',
    '617*......',
    '.....+.58.',  # ....
    '..592.....',  # .58. -> {58} is not adjacent to any symbols
    '......755.',  # ....
    '...$.*....',
    '.664.598..',
]

# The engine schematic (your puzzle input) consists of a visual representation
# of the engine.
# (Periods (.) do not count as a symbol.)

# ANY NUMBER ADJACENT TO A SYMBOL, even DIAGONALLY, is a "part number" and
# should be included in your sum
# add up all the part numbers

# NOT_EVEN_SYMBOL = '.'
RE_DIGIT = r'\d+'
RE_SYMBOL = r'[^\w\s.]'


def day3part1():
    file = open('./input/3.txt', 'r')
    input = file.read().splitlines()

    row_length = len(input[0])
    dummy_row = '.' * row_length

    sum = 0
    for i, row in enumerate(input):
        first_row = i == 0
        last_row = i == len(input) - 1
        row_above = dummy_row if first_row else input[i - 1]
        row_above = 'x' + row_above + 'x'
        row = 'x' + row + 'x'
        row_below = dummy_row if last_row else input[i + 1]
        row_below = 'x' + row_below + 'x'

        # print(row_above)
        # print(row)
        # print(row_below)
        # print()
        for digit in re.finditer(RE_DIGIT, row):
            start = digit.start() - 1
            end = digit.end() + 1

            around_above = row_above[start:end]
            around_number = row[start:end]
            around_below = row_below[start:end]

            symbol_above = re.findall(RE_SYMBOL, around_above)
            symbol_next_to = re.findall(RE_SYMBOL, around_number)
            symbol_below = re.findall(RE_SYMBOL, around_below)

            # print(around_above, symbol_above)
            # print(around_number, symbol_next_to)
            # print(around_below, symbol_below)
            # print()

            around = symbol_above + symbol_next_to + symbol_below
            if around:
                sum += int(digit.group())

    return sum


# print(day3part1())

GEAR = '*'
RE_GEAR = r'\*+'


def day3part2():
    file = open('./input/3.txt', 'r')
    input = file.read().splitlines()
    # input = input1

    row_length = len(input[0])
    dummy_row = '.' * row_length

    sum = 0
    for i, row in enumerate(input):
        first_row = i == 0
        last_row = i == len(input) - 1
        row_above = dummy_row if first_row else input[i - 1]
        row_above = 'x' + row_above + 'x'
        row = 'x' + row + 'x'
        row_below = dummy_row if last_row else input[i + 1]
        row_below = 'x' + row_below + 'x'

        for gear in re.finditer(RE_GEAR, row):
            start = gear.start() - 1 - 2
            end = gear.end() + 1 + 2
            part_numbers = []

            around_above = row_above[start:end]
            around_gear = row[start:end]
            around_below = row_below[start:end]

            symbol_above = re.finditer(RE_DIGIT, around_above)
            symbol_next_to = re.finditer(RE_DIGIT, around_gear)
            symbol_below = re.finditer(RE_DIGIT, around_below)

            # print(around_above)
            # print(around_gear, symbol_next_to)
            # print(around_below)

            for x in symbol_above:
                out_of_bounds = x.start() > 4 or x.end() < 3
                if not out_of_bounds:
                    part_numbers.append((x.group()))

            for x in symbol_next_to:
                out_of_bounds = x.start() > 4 or x.end() < 3
                if not out_of_bounds:
                    part_numbers.append((x.group()))

            for x in symbol_below:
                out_of_bounds = x.start() > 4 or x.end() < 3
                if not out_of_bounds:
                    part_numbers.append((x.group()))

            if (len(part_numbers) == 2):
                sum += int(part_numbers[0]) * int(part_numbers[1])
            # print('gearration', part_numbers)
            # print()
    return sum


print(day3part2())
