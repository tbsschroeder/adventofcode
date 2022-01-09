from lib import get_input
import itertools


def enhance(enhancement, grid, x, y, values, default):
    index = [values.get((x + dx, y + dy), default) for dy, dx in grid]
    return enhancement[int(''.join(index), 2)]


def part1and2():
    enhancement, raw_image = get_input('./input/input20.txt', '\n\n')

    enhancement = [str('.#'.index(x)) for x in enhancement]
    data = {(x, y): str('.#'.index(pixel))
            for y, row in enumerate(raw_image.split('\n'))
            for x, pixel in enumerate(row)}
    grid = list(itertools.product((-1, 0, 1), repeat=2))
    adj = lambda d: {(x + dx, y + dy) for x, y in d for dy, dx in grid}

    for i in range(50):
        default = enhancement[0] if i % 2 else '0'
        data = {(x, y): enhance(enhancement, grid, x, y, data, default) for x, y in adj(data)}
        if i == 1 or i == 49:
            print(sum(p == '1' for p in data.values()))


if __name__ == "__main__":
    part1and2()
