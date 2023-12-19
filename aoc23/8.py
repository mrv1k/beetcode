# expected 2 steps
simple_input = """\
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

# expected 6 steps
loopy_input = """\
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

# Navigate network using left/right. Get from AAA to ZZZ. Counts steps


def day8part1():
    f = open('./input/8.txt', 'r')
    file = f.read().splitlines()
    f.close()
    # file = simple_input.splitlines()
    # file = loopy_input.splitlines()

    instructions = file[0]
    file = file[2:]
    print(instructions)

    current = 'AAA'
    i = 0
    apple_watch = 0

    while current != 'ZZZ':
        for line in file:
            node, crossroads = line.split(' = ')
            if node != current:
                # print('skip', node)
                continue

            left, right = crossroads.replace(
                '(', '').replace(')', '').replace(',', '').split()

            step = instructions[i]
            apple_watch += 1
            i = (i + 1) % len(instructions)
            current = left if step == 'L' else right
            # print(node, step, current)
            if current == 'ZZZ':
                # print('yay')
                return apple_watch


print(day8part1())
