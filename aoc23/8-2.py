input = """\
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""

# It's going to take significantly more steps to escape!
# start at every node that ends with A


def day8part2():
    f = open('./input/8.txt', 'r')
    file = f.read().splitlines()
    f.close()
    # file = simple_input.splitlines()
    # file = loopy_input.splitlines()

    instructions = file[0]
    file = file[2:]

day8part2()
