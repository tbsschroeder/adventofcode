from lib import get_input


def part1(noun: int, verb: int):
    data = get_input('./input/input02.txt', ',')
    data = [int(d) for d in data]
    data[1] = noun
    data[2] = verb
    i = 0
    while data[i] != 99:
        pos1 = data[i + 1]
        pos2 = data[i + 2]
        res = data[i + 3]
        if data[i] == 1:
            data[res] = data[pos1] + data[pos2]
        elif data[i] == 2:
            data[res] = data[pos1] * data[pos2]
        else:
            break
        i += 4
    return data


def part2():
    for noun in range(0, 100):
        for verb in range(0, 100):
            data = part1(noun, verb)
            if data[0] == 19690720:
                return 100 * data[1] + data[2]
    return "ERR"


if __name__ == "__main__":
    print(part1(12, 2)[0])
    print(part2())
