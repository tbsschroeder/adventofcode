from lib import get_input


def slopeit(data, toRight, toBottom):
    trees = 0
    right = 0
    row = 0
    while row < len(data):
        if data[row][right] == '#':
            trees += 1
        right = (right + toRight) % len(data[row])
        row += toBottom
    return trees


def part1():
    data = get_input('./input/input03.txt', '\n')
    print(slopeit(data, 3, 1))


def part2():
    data = get_input('./input/input03.txt', '\n')
    a = slopeit(data, 1, 1)
    b = slopeit(data, 3, 1)
    c = slopeit(data, 5, 1)
    d = slopeit(data, 7, 1)
    e = slopeit(data, 1, 2)
    print(a*b*c*d*e)


if __name__ == "__main__":
    part1()
    part2()
