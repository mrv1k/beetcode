import re


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
            for category_map in maps:
                for m in maps[category_map]:
                    # print(category_map, m)
                    # if start 50, 98, 2 end 51, 99. so 50 -> 98, 51 -> 99, etc
                    destination_start, source_start, range_len = m
                    range_len -= 1  # subtract one to make easier to compute
                    destination_end = destination_start + range_len
                    source_end = source_start + range_len
                    if path >= source_start and path <= source_end:
                        diff = destination_end - source_end
                        # print(category_map, path, '+', diff, '=', path + diff)
                        # print(source_start, source_end, '|', destination_start, destination_end)
                        path += diff
                        locations[i] = path
                        # found a path, break out of this map
                        break
        return min(locations)

print(day5part1())

