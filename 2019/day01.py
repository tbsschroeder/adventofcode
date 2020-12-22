import math
from lib import get_input

def part1():
    data = get_input('./input/input01.txt', '\n')
    res = sum([math.floor(int(line) / 3) - 2 for line in data])
    print(res)

def part2():
    data = get_input('./input/input01.txt', '\n')
    res = 0
    for line in data:
        tmp = int(line)
        while tmp > 0:
            tmp = math.floor(tmp / 3) - 2
            res += tmp if tmp > 0 else 0
    print(res)


if __name__ == "__main__":
    part1()
    part2()
