from lib import get_input


def move(matrix, sym):
    for i, l in enumerate(matrix):
        ll = l[0]
        l = (l + l[0]).replace(f'{sym}.', f'.{sym}')
        matrix[i] = ''.join(l[-1] + l[1:-1]) if l[-1] != ll else ''.join(l[:-1])
    return matrix


def part1():
    matrix = [line.strip() for line in get_input('./input/input25.txt', '\n')]

    step = 1
    while 1:
        step += 1
        right_next = [''.join(line) for line in zip(*move(matrix, '>'))]
        down_new = [''.join(line) for line in zip(*move(right_next, 'v'))]
        if matrix == down_new:
            return step + 3
        matrix = down_new

if __name__ == "__main__":
    print(part1())
