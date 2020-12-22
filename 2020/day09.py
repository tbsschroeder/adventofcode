from lib import get_input
import itertools


def part1():
    data = [int(line) for line in get_input('./input/input09.txt', '\n')]
    c = 25
    index = 0
    while index + c < len(data) - 1:
        preamble = data[index:index + c]
        next_no = data[index + c]
        possible_res = [
            x + y for (x, y) in itertools.permutations(preamble, 2)]
        if next_no not in possible_res:
            print(next_no)
            return next_no
        index += 1


def part2(targetSum):
    data = [int(line) for line in get_input('./input/input09.txt', '\n')]

    for i in range(len(data)):
        for j in range(i-1):
            if sum(data[j:i+1]) == targetSum:
                print(min(data[j:i+1]) + max(data[j:i+1]))
                return


if __name__ == "__main__":
    targetSum = part1()
    part2(targetSum)
