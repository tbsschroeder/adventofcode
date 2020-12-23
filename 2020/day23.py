from lib import get_raw_input


def part1():
    data = get_raw_input('./input/input23.txt')
    cups = [*map(int, list(data))]
    current_cup = 0

    for _ in range(100):
        pickup1 = cups[(current_cup + 1) % len(cups)]
        pickup2 = cups[(current_cup + 2) % len(cups)]
        pickup3 = cups[(current_cup + 3) % len(cups)]
        dest_cup = cups[current_cup] - 1
        current_cup = cups[current_cup]

        cups.remove(pickup1)
        cups.remove(pickup2)
        cups.remove(pickup3)

        while dest_cup not in cups:
            dest_cup = dest_cup - 1 if dest_cup > 1 else 9

        cups.insert(cups.index(dest_cup) + 1, pickup3)
        cups.insert(cups.index(dest_cup) + 1, pickup2)
        cups.insert(cups.index(dest_cup) + 1, pickup1)
        current_cup = (cups.index(current_cup) + 1) % len(cups)

    print(''.join(map(str, cups[cups.index(1) + 1:] + cups[:cups.index(1)])))


def part2():
    data = get_raw_input('./input/input23.txt')
    cups = [*map(int, list(data))]
    ls = {}

    for i in range(1000000):
        if i < len(cups) - 1:
            ls[cups[i]] = cups[i + 1]
        elif i == len(cups) - 1:
            ls[cups[-1]] = max(cups) + 1
        else:
            ls[i + 1] = (i + 2)

    ls[1000000] = cups[0]

    current_cup = cups[0]

    for _ in range(10000000):
        cup1 = ls[current_cup]
        cup2 = ls[cup1]
        cup3 = ls[cup2]

        ls[current_cup] = ls[cup3]
        dest_cup = 1000000 if current_cup == 1 else current_cup - 1

        while dest_cup in [cup1, cup2, cup3]:
            dest_cup = 1000000 if dest_cup == 1 else dest_cup - 1

        ls[cup3] = ls[dest_cup]
        ls[dest_cup] = cup1
        current_cup = ls[current_cup]

    print(ls[1] * ls[ls[1]])


if __name__ == "__main__":
    part1()
    part2()
