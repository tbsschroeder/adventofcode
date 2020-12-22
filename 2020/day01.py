import itertools
from lib import get_input


def part1():
    data = get_input('./input/input01.txt', '\n')
    no_data = [int(line) for line in data]
    for (x, y) in itertools.product(no_data, repeat=2):
        if (x + y == 2020):
            print(f'{x}+{y}=2020 and {x}*{y}={x*y}')
            return


def part2():
    data = get_input('./input/input01.txt', '\n')
    no_data = [int(line) for line in data]
    for (x, y, z) in itertools.product(no_data, repeat=3):
        if (x + y + z == 2020):
            print(f'{x}+{y}+{z}=2020 and {x}*{y}*{z}={x*y*z}')
            return


if __name__ == "__main__":
    part1()
    part2()
