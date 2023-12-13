from functools import reduce

# go farther in each race
# Holding down the button charges the boat
# releasing the button allows the boat to move


def day6part1():
    with open('./input/6.txt', 'r') as file:
        times = map(int, file.readline().split()[1:])
        distances = map(int, file.readline().split()[1:])
        distances = list(distances)
        record_pairs = []
        for i, time in enumerate(times):
            record_pairs.append((time, distances[i]))

        print(record_pairs)
        ways_to_beat = []

        for record in record_pairs:
            the_meat = 0
            hodl = 0
            while hodl < record[0] - 1:
                hodl += 1
                travel = hodl * (record[0] - hodl)
                beat = travel > record[1]
                if beat:
                    the_meat += 1
            ways_to_beat.append(the_meat)
        print(ways_to_beat)
        return reduce(lambda x, y: x * y, ways_to_beat)


print(day6part1())


def day6part2():
    with open('./input/6.txt', 'r') as file:
        times = int(''.join(file.readline().split()[1:]))
        distances = int(''.join(file.readline().split()[1:]))
        record = [times, distances]
        print(times, distances)

        ways_to_beat = []

        the_meat = 0
        hodl = 0
        while hodl < record[0] - 1:
            hodl += 1
            travel = hodl * (record[0] - hodl)
            beat = travel > record[1]
            if beat:
                the_meat += 1
        ways_to_beat.append(the_meat)
        print(ways_to_beat)
        return reduce(lambda x, y: x * y, ways_to_beat)


print(day6part2())
