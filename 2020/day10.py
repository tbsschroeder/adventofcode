from lib import get_input
from collections import defaultdict
from functools import lru_cache


def part1():
    data = [int(line) for line in get_input('./input/input10.txt', '\n')]
    data = [0] + sorted(data)

    diffs = {1: 0, 3: 1}
    for i in range(1, len(data)):
        diffs[data[i] - data[i-1]] += 1
    print(diffs[1] * diffs[3])


def part2():
    data = [int(line) for line in get_input('./input/input10.txt', '\n')]
    data = [0] + sorted(data)

    links = defaultdict(list)
    links = {j: [x for x in data if x < j and x >= j - 3] for j in data}

    @lru_cache(maxsize=len(data))
    def count_paths(pos):
        if pos == 0:
            return 1
        return sum([count_paths(jolt) for jolt in links[pos]])
    print(count_paths(max(data)))


if __name__ == "__main__":
    part1()
    part2()
