import re
from queue import Queue


def day5part1():
    with open('input/5.txt', 'r') as f:
        seed_line = f.readline()
        seeds = re.findall(r'\d+', seed_line.split(": ")[1])
        seeds = list(map(lambda s: int(s), seeds))
        # skip seed new line
        seed_line = f.readline()
        maps = {}
        # print(seeds)
        title = ''
        for line in f:
            line = line.strip()
            line_split = line.split(' ')
            is_title = len(line_split) == 2
            if len(line) == 0:
                continue
            elif is_title:
                title = line_split[0]
                maps[title] = []
            else:
                line_split = list(map(lambda s: int(s), line_split))
                maps[title].append(line_split)

        locations = [0] * len(seeds)
        for i, seed in enumerate(seeds):
            path = seed
            # print('seed', seed)
            for category_key in maps:
                for m in maps[category_key]:
                    # print(category_key, m)
                    # if start 50, 98, 2 end 51, 99. so 50 -> 98, 51 -> 99, etc
                    destination_start, source_start, range_len = m
                    range_len -= 1  # subtract one to make easier to compute
                    destination_end = destination_start + range_len
                    source_end = source_start + range_len
                    if path >= source_start and path <= source_end:
                        diff = destination_end - source_end
                        # print(category_key, path, '+', diff, '=', path + diff)
                        # print(source_start, source_end, '|', destination_start, destination_end)
                        path += diff
                        locations[i] = path
                        # found a path, break out of this map
                        break
        return min(locations)


# print(day5part1())


def day5part2():
    with open('input/example.txt', 'r') as f:
        seed_line = f.readline()
        seeds = re.findall(r'\d+', seed_line.split(": ")[1])
        seeds = list(map(lambda s: int(s), seeds))

        sweet_milky = []
        for i in range(0, len(seeds), 2):
            seed_start = seeds[i]
            seed_step = seeds[i + 1]
            sweet_milky.append((seed_start, seed_start + seed_step))
        seeds = sweet_milky
        # print(sweet_milky)

        # skip seed new line
        seed_line = f.readline()
        maps = {}
        title = ''
        for line in f:
            line = line.strip()
            line_split = line.split(' ')
            is_title = len(line_split) == 2
            if len(line) == 0:
                continue
            elif is_title:
                title = line_split[0]
                maps[title] = []
            else:
                line_split = list(map(lambda s: int(s), line_split))
                # if start 50, 98, 2 end 51, 99. so 50 -> 98, 51 -> 99, etc
                destination_start, source_start, range_len = line_split
                range_len -= 1  # subtract one to make easier to compute
                source = (source_start, source_start + range_len)
                destination = (destination_start,
                               destination_start + range_len)
                maps[title].append((source, destination))

        print(seeds)
        min_seed = float('inf')
        queue = Queue()
        for i, pair_of_seeds in enumerate(seeds):
            # queue.put(1) queue.get()
            path = pair_of_seeds
            print(pair_of_seeds)
            for map_key in maps:
                for map_value in maps[map_key]:
                    source, destination = map_value
                    source_start, source_end = source
                    destination_start, destination_end = destination

                    inner_join = path[0] >= source_start and path[1] <= source_end
                    left_join = path[0] >= source_start and path[1] >= source_end
                    right_join = path[0] >= source_start and path[1] <= source_end
                    full_join = path[0] <= source_start and path[1] >= source_end
                    print(path[0], path[1], source_start,  source_end)
                    print('in', inner_join, '| left', left_join,
                          '| right', right_join, '| full', full_join)
                    print(map_key, map_value)

                    if inner_join:
                        print()
                        # dts = destination_end - source_end
                        # after = path + dts
                        # print(path, '+', dts, '=', after)
                        # path = after
                        # found a path, break out of this map
                        break
            min_seed = min(min_seed, path)
            return min_seed
            # print('final path', path)
        return min_seed


print(day5part2())
