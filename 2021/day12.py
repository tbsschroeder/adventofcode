from lib import get_input
from collections import defaultdict
neighbours = defaultdict(list)


def count(part, seen=[], cave='start'):
    if cave == 'end':
        return 1
    if cave in seen:
        if cave == 'start':
            return 0
        if cave.islower():
            if part == 1:
                return 0
            else:
                part = 1

    return sum(count(part, seen + [cave], n) for n in neighbours[cave])


def part1and2():
    data = get_input('./input/input12.txt', '\n')
    for line in data:
        a, b = line.split('-')
        neighbours[a] += [b]
        neighbours[b] += [a]

    print(count(part=1))
    print(count(part=2))


if __name__ == "__main__":
    part1and2()
