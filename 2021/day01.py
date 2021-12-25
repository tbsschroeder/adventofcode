from lib import get_input


def part1():
    data = get_input('./input/input01.txt', '\n')
    no_data = [int(line) for line in data]
    depth = [no_data[i - 1] < line for i, line in enumerate(no_data)]
    print(sum(depth))
    return


def part2():
    data = get_input('./input/input01.txt', '\n')
    no_data = [int(line) for line in data]
    windows = [sum(x) for x in zip(no_data, no_data[1:], no_data[2:])]
    pairs = zip(windows, windows[1:])
    depth = [y - x for x, y in pairs if y - x > 0]
    print(len(depth))
    return


if __name__ == "__main__":
    part1()
    part2()
