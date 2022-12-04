from lib import get_input
from operator import methodcaller


def part1():
    sections = [l.split(',') for l in get_input('./input/input04.txt', '\n')]
    amount = 0
    for s1, s2 in sections:
        a, b = list(map(int,s1.split('-')))
        c, d = list(map(int,s2.split('-')))
        l1, l2 = list(range(a, b + 1)), list(range(c, d + 1))
        inter = [el for el in l1 if el in l2]
        if inter == l1 or inter == l2:
            amount += 1
    print(amount)


def part2():
    sections = [l.split(',') for l in get_input('./input/input04.txt', '\n')]
    amount = 0
    for s1, s2 in sections:
        a, b = list(map(int,s1.split('-')))
        c, d = list(map(int,s2.split('-')))
        s1, s2 = set(range(a, b + 1)), set(range(c, d + 1))
        inter = [el for el in s1 if el in s2]
        if not s1.isdisjoint(s2):
            amount += 1
    print(amount)

if __name__ == "__main__":
    part1()
    part2()
