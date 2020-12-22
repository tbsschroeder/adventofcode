from lib import get_input
from collections import defaultdict
from itertools import product

INPUT_ACTIVE = '#'
ACTIVE = 1
INACTIVE = 0


def get_neighbors(loc):
    offsets = product((-1, 0, 1), repeat=len(loc))
    neighbors = set()
    for offset in offsets:
        if offset == (0,) * len(loc):
            continue
        neighbors.add(tuple(a + b for a, b in zip(loc, offset)))
    return neighbors


def get_all_neighbors(locs):
    return set.union(*(get_neighbors(loc) for loc in locs))


def initialize(lines, dim):
    start_gen = defaultdict(int)
    for i, line in enumerate(lines):
        for j, letter in enumerate(line):
            if letter == INPUT_ACTIVE:
                start_gen[(i, j) + (0,) * (dim - 2)] = ACTIVE
    return start_gen


def cycle(start, times):
    current_gen = start
    for _ in range(times):
        next_gen = defaultdict(int)
        all_locs = get_all_neighbors(current_gen.keys())
        all_locs.update(current_gen.keys())
        for loc in all_locs:
            neighbors = get_neighbors(loc)
            count = sum(current_gen[n] for n in neighbors)
            if count in (2, 3) and current_gen[loc] == ACTIVE:
                next_gen[loc] = ACTIVE
            elif count == 3 and current_gen[loc] == INACTIVE:
                next_gen[loc] = ACTIVE
        current_gen = next_gen
    return current_gen


def part1():
    data = get_input('./input/input17.txt', '\n')
    start_gen = initialize(data, 3)
    end_gen = cycle(start_gen, 6)
    print(sum(end_gen.values()))


def part2():
    data = get_input('./input/input17.txt', '\n')
    start_gen = initialize(data, 4)
    end_gen = cycle(start_gen, 6)
    print(sum(end_gen.values()))


if __name__ == "__main__":
    part1()
    part2()
