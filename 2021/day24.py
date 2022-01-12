from lib import get_input


if __name__ == "__main__":
    digits = dict()
    stack = list()
    push = sub = dig = 0
    data = get_input('./input/input24.txt', '\n')

    for i, line in enumerate(data):
        _, *operands = line.rstrip().split(' ')
        if i % 18 == 4:
            push = operands[1] == '1'
        if i % 18 == 5:
            sub = int(operands[1])
        if i % 18 == 15:
            if push:
                stack.append((dig, int(operands[1])))
            else:
                sibling, add = stack.pop()
                diff = add + sub
                if diff < 0:
                    digits[sibling] = (-diff + 1, 9)
                    digits[dig] = (1, 9 + diff)
                else:
                    digits[sibling] = (1, 9 - diff)
                    digits[dig] = (1 + diff, 9)
            dig += 1

    print(''.join(str(digits[d][1]) for d in sorted(digits.keys())))
    print(''.join(str(digits[d][0]) for d in sorted(digits.keys())))
