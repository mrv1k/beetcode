from functools import reduce

input = open('./input/2.txt', 'r')
input1 = [
    'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',  # True
    'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',  # True
    'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',  # False
    'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',  # False
    'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',  # True
]
# expected ID sum = 8. 1 + 2 + 5

RED, GREEN, BLUE = 12, 13, 14

# The Elf would first like to know which games would have been possible if
# the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
# What is the sum of the IDs of those games?


def day2part1():
    game_number = 1
    sum = 0

    for row in input:
        draws = row.split(':')[1]
        sets = draws.split(';')
        possible = True
        # print(sets)
        for s in sets:
            # print(s)
            colors = s.split(',')
            # print(colors)
            for color in colors:
                # print(color)
                if 'red' in color:
                    v = color.replace('red', '').strip()
                    if int(v) > RED:
                        possible = False
                        break
                elif 'green' in color:
                    v = color.replace('green', '').strip()
                    if int(v) > GREEN:
                        possible = False
                        break
                elif 'blue' in color:
                    v = color.replace('blue', '').strip()
                    if int(v) > BLUE:
                        possible = False
                        break
        if possible:
            sum = sum + game_number

        game_number += 1

    return sum


# print(day2part1())

# For each game, find the MINIMUM SET OF CUBES that must have been present.
# What is the sum of the power of these sets?
# eg: Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.


def day2part2():
    sum = 0

    for row in input:
        draws = row.split(':')[1]
        sets = draws.split(';')
        max_d = {'red': 0, 'green': 0, 'blue': 0}
        for s in sets:
            colors = s.split(',')
            for color in colors:
                if 'red' in color:
                    v = color.replace('red', '').strip()
                    max_d['red'] = max(max_d['red'], int(v))
                elif 'green' in color:
                    v = color.replace('green', '').strip()
                    max_d['green'] = max(max_d['green'], int(v))
                elif 'blue' in color:
                    v = color.replace('blue', '').strip()
                    max_d['blue'] = max(max_d['blue'], int(v))

        power = reduce(lambda x, y: x * y, max_d.values())
        sum += power

    return sum


print(day2part2())
