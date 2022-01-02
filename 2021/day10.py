from lib import get_input


def is_match(open_char, close_char):
    return open_char == '(' and close_char == ')' or \
        open_char == '{' and close_char == '}' or \
        open_char == '[' and close_char == ']' or \
        open_char == '<' and close_char == '>'

def get_score(char):
    if char == ')':
        return 3
    if char == ']':
        return 57
    if char == '}':
        return 1197
    if char == '>':
        return 25137

def parse(line):
    tree = []
    for char in list(line):
        if char in ['(', '[', '{', '<']:
            tree.append(char)
        elif is_match(tree[-1], char):
            tree = tree[:-1]
        else:
            return get_score(char)
    return 0


def part1():
    data = get_input('./input/input10.txt', '\n')
    score = 0
    for line in data:
        score += parse(line)
    print(score)


def part2():
    data = get_input('./input/input10.txt', '\n')
    print(0)


if __name__ == "__main__":
    part1()
    part2()
