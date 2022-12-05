from lib import get_input


def part1and2():
    sections = [line.split(',') for line in get_input('./input/input04.txt', '\n')]
    joints, disjoints = 0, 0
    for s1, s2 in sections:
        a, b = list(map(int, s1.split('-')))
        c, d = list(map(int, s2.split('-')))
        l1, l2 = list(range(a, b + 1)), list(range(c, d + 1))
        inter = [el for el in l1 if el in l2]
        if inter == l1 or inter == l2:
            joints += 1
        if not set(l1).isdisjoint(set(l2)):
            disjoints += 1
    print(joints)
    print(disjoints)


if __name__ == "__main__":
    part1and2()
