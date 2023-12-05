import re
input1 = [  # #      ∅∅∅∅∅
    '467..114..',  # .114. -> {114} is not adjacent to any symbols
    '...*......',  # .....
    '..35..633.',
    '......#...',
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

file = open('./input/3.txt', 'r')


def day3part1():
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
            # print(around_above, symbol_above)
            # print(around_number, symbol_next_to)
            # print(around_below, symbol_below)
            # print()

            symbol_above = re.findall(RE_SYMBOL, around_above)
            symbol_next_to = re.findall(RE_SYMBOL, around_number)
            symbol_below = re.findall(RE_SYMBOL, around_below)

            around = symbol_above + symbol_next_to + symbol_below
            if around:
                sum += int(digit.group())

    return sum


print(day3part1())


def day3part2():
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
            # print(around_above, symbol_above)
            # print(around_number, symbol_next_to)
            # print(around_below, symbol_below)
            # print()

            symbol_above = re.findall(RE_SYMBOL, around_above)
            symbol_next_to = re.findall(RE_SYMBOL, around_number)
            symbol_below = re.findall(RE_SYMBOL, around_below)

            around = symbol_above + symbol_next_to + symbol_below
            if around:
                sum += int(digit.group())

    return sum


print(day3part2())
