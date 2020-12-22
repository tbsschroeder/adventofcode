from lib import get_input
import re


def eval_1(text: str) -> int:
    if ms := re.search(r"(\((\d+)(\s([+*])\s(\d+))+\))", text):
        tmp = text.replace(ms.groups()[0], str(
            eval_1(ms.groups()[0][1:-1])), 1)
        return eval_1(tmp)
    if ms := re.match(r"(\d+)\s([+*])\s(\d+)", text):
        x, op, y = ms.groups()
        mul_add = int(x) + int(y) if op == "+" else int(x) * int(y)
        return eval_1(text.replace(ms.group(), str(mul_add), 1))
    return int(text)


def eval_2(text: str) -> int:
    if ms := re.search(r"(\((\d+)(\s([+*])\s(\d+))+\))", text):
        tmp = text.replace(ms.groups()[0], str(
            eval_2(ms.groups()[0][1:-1])), 1)
        return eval_2(tmp)
    if ms := re.search(r"(\d+)\s\+\s(\d+)", text):
        add = int(ms.groups()[0]) + int(ms.groups()[1])
        tmp = text.replace(ms.group(), str(add), 1)
        return eval_2(tmp)
    if ms := re.match(r"(\d+)\s\*\s(\d+)", text):
        mul = int(ms.groups()[0]) * int(ms.groups()[1])
        tmp = text.replace(ms.group(), str(mul), 1)
        return eval_2(tmp)
    return int(text)


def part1():
    data = get_input('./input/input18.txt', '\n')
    print(sum([eval_1(line) for line in data]))


def part2():
    data = get_input('./input/input18.txt', '\n')
    print(sum([eval_2(line) for line in data]))


if __name__ == "__main__":
    # time to learn the walrus operator and mor regex
    part1()
    part2()
