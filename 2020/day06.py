from lib import get_input


def part1():
    data = get_input('./input/input06.txt', '\n\n')
    print(sum([len(set(g.replace('\n', ''))) for g in data]))


def part2():
    data = get_input('./input/input06.txt', '\n\n')
    print(sum([len(set.intersection(*[set(g) for g in g.split('\n')]))
               for g in data]))


if __name__ == "__main__":
    part1()
    part2()
