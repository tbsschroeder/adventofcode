from lib import get_input

div = 20201227


def part1():
    p1, p2 = [*map(int, get_input('./input/input25.txt', '\n'))]

    loop = 0
    subject = 7
    acc = 1
    circle = 20201227
    while acc != p1:
        acc = (acc*subject) % circle
        loop = loop + 1

    print(pow(p2, loop, circle))


def part2():
    p1, p2 = [*map(int, get_input('./input/input25.txt', '\n'))]


if __name__ == "__main__":
    part1()
    part2()
