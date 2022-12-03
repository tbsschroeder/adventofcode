from lib import get_input


def get_prio(c):
    return ord(c) - (38 if c.isupper() else 96)


def part1():
    print(sum(get_prio(char) for char in (c.pop() for c in (set(line[:len(line) // 2]).intersection(set(line[len(line) // 2:])) for line in get_input('./input/input03.txt', '\n')))))


def part2():
    print(sum([(*range(-38, 59), *range(1, 27))[ord(set.intersection(*map(set, L)).pop())] for L in zip(*[map(list, open('./input/input03.txt').read().split()[i::3])for i in (0, 1, 2)])]))


if __name__ == "__main__":
    part1()
    part2()
