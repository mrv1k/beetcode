import re
input1 = [  # #      ∅∅∅∅∅
    '467..114..',  # .114. -> {114} is not adjacent to any symbols
    '...*......',  # .....
    '..35..633.',
    '......#...',
    # '*111#...',
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
    # file = open('./input/3.txt', 'r')
    # input = file.read().splitlines()
    input = input1

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

        # if i == 3:
        #     return 0

        # print(row_above)
        # print(row)
        # print(row_below)
        # print()
        for gear in re.finditer(RE_GEAR, row):
            start = gear.start() - 1 - 2
            end = gear.end() + 1 + 2

            around_above = row_above[start:end]
            around_gear = row[start:end]
            around_below = row_below[start:end]

            # print(''.join(around_above + around_gear + around_below))

            symbol_above = re.finditer(RE_DIGIT, around_above)
            symbol_next_to = re.findall(RE_DIGIT, around_gear)
            symbol_below = re.findall(RE_DIGIT, around_below)

            # start = gear.start() - 1 - 2
            # end = gear.end() + 1 + 2
            # bigger_above = row_above[start:end]

            print(around_above, symbol_above)
            print(around_gear, symbol_next_to, gear.start(), gear.end())
            print(around_below, symbol_below)
            print()
            for x in symbol_above:
                # y = around_above.find(x)
                print(x, gear)
            # a = len(symbol_above) > 0 and len(symbol_above[0]) < 3
            # if a:
            #     print(bigger_above, bigger_above.find(symbol_above[0]))
            # print()

            # around = symbol_above + symbol_next_to + symbol_below
            # if around:
            #     sum += int(digit.group())

    return sum


print(day3part2())

# start = gear.start() - 1 - 2
# end = gear.end() + 1 + 2
# bigger_above = row_above[start:end]
# above_i = bigger_above.find(symbol_above[0])
# print(bigger_above, i, row_above[:above_i+1], row_above[above_i:])
# #
# k = len(symbol_above) > 0 and len(symbol_above[0]) < 3
# o = row_above[start - 2:end + 2]
