from lib import get_input

corrupted = []
incomplete = []


def is_match(open_char, close_char):
    closer = {'(': ')', '[': ']', '{': '}', '<': '>'}
    return closer[open_char] == close_char


def get_first_error_score(line):
    stack = []
    values = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    for char in line:
        if char in ['(', '[', '{', '<']:
            stack.append(char)
        elif is_match(stack[-1], char):
            stack.pop()
        else:
            corrupted.append(line)
            return values[char]
    incomplete.append(line)
    return 0


def get_closing_character_values(line):
    cost = {')': 1, ']': 2, '}': 3, '>': 4}
    opener = {')': '(', ']': '[', '}': '{', '>': '<'}
    closer = {'(': ')', '[': ']', '{': '}', '<': '>'}

    stack = []
    score = 0
    for char in line:
        if char in closer:
            stack.append(char)
        elif stack.pop() != opener[char]:
            break
    else:
        while len(stack) > 0:
            char = closer[stack.pop()]
            score = score * 5 + cost[char]
        return score


def part1():
    data = get_input('./input/input10.txt', '\n')
    scores = [get_first_error_score(list(line)) for line in data]
    print(sum(scores))


def part2():
    scores = [get_closing_character_values(list(line)) for line in incomplete]
    print(sorted(scores)[len(scores) // 2])


if __name__ == "__main__":
    part1()
    part2()
