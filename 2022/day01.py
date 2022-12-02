from lib import get_input


def part1():
    print(max([sum(list(map(int, line.split('\n')))) for line in get_input('./input/input01.txt', '\n\n')]))


def part2():
    calories = [sum(list(map(int, line.split('\n')))) for line in get_input('./input/input01.txt', '\n\n')]
    calories.sort()
    print(sum(calories[-3:]))


if __name__ == "__main__":
    part1()
    part2()
