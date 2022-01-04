from lib import get_input
from collections import Counter


def get_repl(replacements, char):
    if char in replacements.keys():
        return char[0] + replacements[char]
    return char


def print_diff_in_polymer(count):
    template, data = get_input('./input/input14.txt', '\n\n')
    instructions = dict(d.split(" -> ") for d in data.split('\n'))
    pairs = Counter(map(str.__add__, template, template[1:]))
    chars = Counter(template)

    for _ in range(0, count):
        for (a, b), c in pairs.copy().items():
            x = instructions[a + b]
            pairs[a + b] -= c
            pairs[a + x] += c
            pairs[x + b] += c
            chars[x] += c
    print(max(chars.values()) - min(chars.values()))


def part1():
    print_diff_in_polymer(10)


def part2():
    print_diff_in_polymer(40)


if __name__ == "__main__":
    part1()
    part2()
