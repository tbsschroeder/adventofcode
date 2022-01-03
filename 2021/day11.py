from lib import get_input


def part1and2():
    octopuses = {
        complex(row, col): int(number)
        for row, line in enumerate(get_input('./input/input11.txt', '\n'))
        for col, number in enumerate(line)
    }

    step, part1, part2 = 0, 0, None

    while step := step + 1:
        flashing, flashed = set(), set()

        for octo in octopuses.keys():
            octopuses[octo] += 1
            if octopuses[octo] > 9:
                flashing.add(octo)

        while flashing:
            octo = flashing.pop()
            octopuses[octo] = 0
            flashed.add(octo)

            for i in (
                    -1 + 1j, -1j, +1 + 1j,
                    -1, +1,
                    -1 - 1j, +1j, +1 - 1j
            ):
                if (x := octo + i) in octopuses and x not in flashed:
                    octopuses[x] += 1
                    if octopuses[x] > 9:
                        flashing.add(x)

        if part2 is None and len(flashed) == len(octopuses):
            part2 = step

        if step <= 100:
            part1 += len(flashed)
        elif part2:
            break

    print(part1)
    print(part2)


if __name__ == "__main__":
    part1and2()
