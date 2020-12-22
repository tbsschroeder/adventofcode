from lib import get_input
from collections import defaultdict


def memory(numbers, rounds):
    spoken = defaultdict(int)
    index = 0
    for turn in range(1, rounds + 1):
        if index != len(numbers):
            spoken[numbers[index]] = turn
            said = numbers[index]
            next_no = 0
            index += 1
            continue
        said = next_no
        next_no = (turn - spoken[next_no]) if next_no in spoken else 0
        spoken[said] = turn
    print(said)


def part1():
    data = get_input('./input/input15.txt', '\n')
    numbers = [int(d) for d in data[0].split(',')]
    memory(numbers, 2020)


def part2():
    data = get_input('./input/input15.txt', '\n')
    numbers = [int(d) for d in data[0].split(',')]
    memory(numbers, 30000000)


if __name__ == "__main__":
    part1()
    part2()
