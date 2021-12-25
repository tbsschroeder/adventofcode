from lib import get_input


def part1():
    data = [line for line in get_input('./input/input03.txt', '\n')]
    chars = [[char for char in word] for word in data]
    transposed = list(map(list, zip(*chars)))

    gamma = ''
    epsilon = ''
    for t in transposed:
        gamma += '1' if t.count('1') > t.count('0') else '0'
        epsilon += '0' if t.count('1') > t.count('0') else '1'
    print(eval('0b' + gamma) * eval('0b' + epsilon))


def part2():
    data = [line.split() for line in get_input('./input/input03.txt', '\n')]
    chars = [[char for char in word] for word in data]
    transposed = list(map(list, zip(*chars)))


if __name__ == "__main__":
    part1()
    part2()
