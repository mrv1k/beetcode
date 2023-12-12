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
    with open('input/5.txt', 'r') as f:
        seed_line = f.readline()
        seeds = re.findall(r'\d+', seed_line.split(": ")[1])
        seeds = list(map(lambda s: int(s), seeds))

        sweet_milky = []
        for i in range(0, len(seeds), 2):
            seed_start = seeds[i]
            seed_step = seeds[i + 1]
            sweet_milky.append((seed_start, seed_start + seed_step))
        seeds = sweet_milky

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
                # range_len -= 1  # subtract one to make easier to compute
                source = (source_start, source_start + range_len)
                destination = (destination_start,
                               destination_start + range_len)
                maps[title].append((source, destination))

        # seeds = [seeds[0]]
        print(seeds)
        for map_key, map_values in maps.items():
            # print(map_values)
            new = []
            while len(seeds) > 0:
                # print(len(seeds), seeds)
                start, end = seeds.pop()
                for source, destination in map_values:
                    # print(map_key, source, destination, 'from', start, end)
                    ss, se = source
                    destination_start, destination_end = destination

                    overlap_start = max(start, ss)
                    overlap_end = min(end, se)

                    # x = overlap_start < overlap_end
                    # y = overlap_start > start
                    # z = end > overlap_end

                    if overlap_start < overlap_end:
                        new.append((overlap_start - ss + destination_start,
                                   overlap_end - ss + destination_start))
                        if overlap_start > start:
                            seeds.append((start, overlap_start))
                        if end > overlap_end:
                            seeds.append((overlap_end, end))
                        break
                else:
                    new.append((start, end))

            seeds = new
        # print(seeds)
        return min(seeds)[0]


print(day5part2())
