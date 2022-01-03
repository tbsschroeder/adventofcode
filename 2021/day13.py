from lib import get_input


def fold(points, axis, n):
    if axis == 'x':
        return {(y - (y - n) * 2, x) if y > n else (y, x) for y, x in points}
    return {(y, x - (x - n) * 2) if x > n else (y, x) for y, x in points}


def display(points):
    arr = [[' '] * 39 for _ in range(6)]
    for y, x in points:
        arr[x][y] = '#'
    return '\n'.join(''.join(row) for row in arr)


def part1(points):
    axis, n = folds[0]
    return len(fold(points, axis, n))


def part2(points):
    for axis, n in folds:
        points = fold(points, axis, n)
    return display(points)


if __name__ == "__main__":
    data = get_input('./input/input13.txt', '\n\n')
    points = {tuple(map(int, line.split(','))) for line in data[0].split('\n')}
    folds = [(cmd[11], int(cmd[13:])) for cmd in data[1].split('\n')]

    print(part1(points))
    print(part2(points))
