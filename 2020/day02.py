from lib import get_input


def part1():
    data = get_input('./input/input02.txt', '\n')
    valid = 0
    for line in data:
        split = line.replace(':', '').split(' ')
        count = split[0].split('-')
        countStart = int(count[0])
        countEnd = int(count[1])
        char = split[1]
        passwd = split[2]
        if passwd.count(char) >= countStart and passwd.count(char) <= countEnd:
            valid += 1
    print(valid)


def part2():
    data = get_input('./input/input02.txt', '\n')
    valid = 0
    for line in data:
        split = line.replace(':', '').split(' ')
        count = split[0].split('-')
        countStart = int(count[0]) - 1
        countEnd = int(count[1]) - 1
        char = split[1]
        passwd = split[2]
        if passwd[countStart] == char and passwd[countEnd] != char \
                or passwd[countStart] != char and passwd[countEnd] == char:
            valid += 1
    print(valid)


if __name__ == "__main__":
    part1()
    part2()
