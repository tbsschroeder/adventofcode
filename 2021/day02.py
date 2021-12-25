from lib import get_input


def part1():
    data = get_input('./input/input02.txt', '\n')
    coordinates = [line.split(' ') for line in data]
    horizontal = 0
    depth = 0
    for direction, no in coordinates:
        if direction == 'down':
            depth += int(no)
        if direction == 'up':
            depth -= int(no)
        if direction == 'forward':
            horizontal += int(no)
    print(depth * horizontal)


def part2():
    data = get_input('./input/input02.txt', '\n')
    coordinates = [line.split(' ') for line in data]
    horizontal = 0
    depth = 0
    aim = 0
    for direction, no in coordinates:
        if direction == 'down':
            aim += int(no)
        if direction == 'up':
            aim -= int(no)
        if direction == 'forward':
            horizontal += int(no)
            depth += int(no) * aim
    print(depth * horizontal)


if __name__ == "__main__":
    part1()
    part2()
