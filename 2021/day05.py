from lib import get_input
from collections import Counter


def get_values_between(v1, v2, multiplier):
    if v1 > v2:
        return [*range(v1, v2 - 1, -1)]
    elif v1 < v2:
        return [*range(v1, v2 + 1)]
    else:
        return [v1] * multiplier


def get_intersections_count(include_diagonal):
    data = get_input('./input/input05.txt', '\n')

    lines = []
    for line in data:
        (x1, y1), (x2, y2) = [tuple(int(i) for i in x_y.split(','))
                              for x_y in line.split('->')]

        x_dist = abs(x1 - x2)
        y_dist = abs(y1 - y2)

        # is_diagonal = x_dist != 0 and y_dist != 0
        if x_dist != 0 and y_dist != 0 and not include_diagonal:
            continue

        mul = max(x_dist, y_dist) + 1
        x_values = get_values_between(x1, x2, mul)
        y_values = get_values_between(y1, y2, mul)

        for idx, x in enumerate(x_values):
            lines.append(((x, y_values[idx])))

    count = Counter(lines)
    return len([i for i in count.values() if i > 1])


def part1():
    print(get_intersections_count(False))


def part2():
    print(get_intersections_count(True))


if __name__ == "__main__":
    part1()
    part2()
