from lib import get_input
from collections import Counter


def part1and2():
    lines = [line for line in get_input('./input/input23.txt', '\n')]
    locations = set()
    for i, line in enumerate(lines):
        for j, ch in enumerate(line):
            if ch == '#':
                locations.add((i, j))

    def stay_still(x, y, locations): return all([(x + dx, y + dy) not in locations for (dx, dy) in [(-1, -1), (0, -1), (1, -1), (-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0)]])

    checks = [
        lambda x, y, locations: all([(x + dx, y + dy) not in locations for (dx, dy) in [(-1, -1), (-1, 0), (-1, 1)]]) and (x - 1, y + 0),  # N
        lambda x, y, locations: all([(x + dx, y + dy) not in locations for (dx, dy) in [(1, -1), (1, 0), (1, 1)]]) and (x + 1, y + 0),  # S
        lambda x, y, locations: all([(x + dx, y + dy) not in locations for (dx, dy) in [(-1, -1), (0, -1), (1, -1)]]) and (x + 0, y - 1),  # W
        lambda x, y, locations: all([(x + dx, y + dy) not in locations for (dx, dy) in [(-1, 1), (0, 1), (1, 1)]]) and (x + 0, y + 1),  # E
    ]

    old_locations = locations.copy()
    k = 0
    while True:
        k += 1
        # Part 1
        proposals = {}
        for location in locations:
            if stay_still(location[0], location[1], locations):
                proposals[location] = location
                continue
            for check in checks:
                direction = check(location[0], location[1], locations)
                if direction:
                    proposals[location] = direction
                    break
            if location not in proposals:
                proposals[location] = location

        # Part 2
        valid_targets = set(x[0] for x in Counter(proposals.values()).items() if x[1] == 1)
        filtered_proposals = dict([(x, y) for (x, y) in proposals.items() if y in valid_targets])
        filtered_proposals = dict([(x, y) for (x, y) in filtered_proposals.items() if x != y])

        locations = locations.difference(filtered_proposals.keys())
        locations.update(filtered_proposals.values())

        if old_locations == locations:
            break

        if k == 10:
            w = max([x[0] for x in locations]) - min([x[0] for x in locations]) + 1
            h = max([x[1] for x in locations]) - min([x[1] for x in locations]) + 1
            part1 = w * h - len(locations)
        old_locations = locations.copy()
        # Part 3
        checks.append(checks.pop(0))

    part2 = k

    print(part1, part2)


if __name__ == "__main__":
    part1and2()
