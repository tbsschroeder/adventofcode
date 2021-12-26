from lib import get_input
import numpy as np


def part1():
    data = [line for line in get_input('./input/input03.txt', '\n')]
    chars = [[char for char in word] for word in data]
    transposed = list(map(list, zip(*chars)))

    gamma = ''
    epsilon = ''
    for t in transposed:
        gamma += '1' if t.count('1') >= t.count('0') else '0'
        epsilon += '0' if t.count('1') >= t.count('0') else '1'
    print(eval('0b' + gamma) * eval('0b' + epsilon))


def part2():
    data = get_input('./input/input03.txt', '\n')
    lines = [list(line.strip()) for line in data]
    grid = np.array(lines, dtype=int)
    width = np.shape(grid)[1]

    def filterByMostCommon(col, grid):
        countOne = sum(grid[:, col] == 1)
        countZero = sum(grid[:, col] == 0)
        mostCommon = 1 if countOne >= countZero else 0
        return np.delete(grid, np.where(grid[:, col] != mostCommon)[0], axis=0)

    def filterByLeastCommon(col, grid):
        countOne = sum(grid[:, col] == 1)
        countZero = sum(grid[:, col] == 0)
        leastCommon = 0 if countZero <= countOne else 1
        return np.delete(grid, np.where(grid[:, col] != leastCommon)[0], axis=0)

    grid = np.array(lines, dtype=int)
    column = 0
    while np.shape(grid)[0] > 1:
        grid = filterByMostCommon(column, grid)
        column += 1

    nums = ''.join([str(grid[0, i]) for i in range(width)])
    oxy = int(nums, 2)

    grid = np.array(lines, dtype=int)
    column = 0
    while np.shape(grid)[0] > 1:
        grid = filterByLeastCommon(column, grid)
        column += 1

    nums = ''.join([str(grid[0, i]) for i in range(width)])
    co2 = int(nums, 2)

    print(co2 * oxy)


if __name__ == "__main__":
    part1()
    part2()
