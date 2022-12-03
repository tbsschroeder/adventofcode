from lib import get_input


def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [alist[i * length // wanted_parts: (i + 1) * length // wanted_parts]
            for i in range(wanted_parts)]


def get_prio(c):
    print(c)
    if c.isupper():
        return ord(c) - ord('A') + 27
    else:
        return ord(c) - ord('a') + 1


def part1():
    rucksacks = [line for line in get_input('./input/input03.txt', '\n')]
    compartments = []
    for rucksack in rucksacks:
        [list1, list2] = split_list(rucksack, 2)
        compartments.append(list(set(list1).intersection(list2))[0])
    print(sum(get_prio(c) for c in compartments))


def part2():
    print('')


if __name__ == "__main__":
    part1()
    part2()
