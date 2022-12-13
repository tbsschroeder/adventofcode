from lib import get_input


def part1and2():
    data = [line.split(' ') for line in get_input('./input/input10.txt', '\n')]

    x = 1
    states = []

    for pos, cmd in enumerate(data):
        if len(cmd) == 1:
            states.append(x)
        if len(cmd) == 2:
            states += [x, x]
            x += int(cmd[1])

    print(sum([(i + 1) * val for i, val in enumerate(states) if (i + 1) % 40 - 20 == 0]))

    crt = [
        "##" if i % 40 in list(range(_ - 1, _ + 2)) else '  '
        for i, _ in enumerate(states)
    ]
    crt = [crt[i:i + 40] for i in range(0, len(crt), 40)]
    print("\n".join(["".join(_) for _ in crt]))


if __name__ == "__main__":
    part1and2()
