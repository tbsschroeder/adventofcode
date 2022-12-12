from lib import get_input


def score(trees, x, y):
    h = len(trees)
    w = len(trees[0])

    ret = 1
    for j in range(y - 1, -1, -1):
        if trees[j][x] >= trees[y][x]:
            break

    ret *= y - j
    for j in range(y + 1, h):
        if trees[j][x] >= trees[y][x]:
            break

    ret *= j - y
    for i in range(x - 1, -1, -1):
        if trees[y][i] >= trees[y][x]:
            break

    ret *= x - i
    for i in range(x + 1, w):
        if trees[y][i] >= trees[y][x]:
            break

    ret *= i - x
    return ret


def visible(trees, x, y):
    h = len(trees)
    w = len(trees[0])
    return any([
        all([(trees[y][x] > trees[y][i]) for i in range(0, x)]),
        all([(trees[y][x] > trees[y][i]) for i in range(x + 1, w)]),
        all([(trees[y][x] > trees[j][x]) for j in range(0, y)]),
        all([(trees[y][x] > trees[j][x]) for j in range(y + 1, h)])
    ])


def part1():
    trees = [list(map(int, list(line))) for line in get_input('./input/input08.txt', '\n')]

    h = len(trees)
    w = len(trees[0])

    r1 = 0
    for y in range(h):
        for x in range(w):
            r1 += visible(trees, x, y)

    print(r1)


def part2():
    trees = [list(map(int, list(line))) for line in get_input('./input/input08.txt', '\n')]

    h = len(trees)
    w = len(trees[0])

    r2 = 0
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            r2 = max(r2, score(trees, x, y))

    print(r2)


if __name__ == "__main__":
    part1()
    part2()
