factor_a = 16807
factor_b = 48271
divider = 2147483647


def judge(a, b):
    conv_a = hex(a).split('x')[-1]
    conv_b = hex(b).split('x')[-1]
    return conv_a[-4:] == conv_b[-4:]


def task1(a, b):
    matches = 0
    for i in range(0, 40000000):
        a = (a * factor_a) % divider
        b = (b * factor_b) % divider
        # hint which is faster a & 0xffff == b & 0xffff
        if judge(a, b):
            matches += 1
    print('First solution: {}'.format(matches))


def task2(a, b):
    matches = 0
    for i in range(0, 5000000):
        while True:
            a = (a * factor_a) % divider
            if a % 4 == 0:
                break
        while True:
            b = (b * factor_b) % divider
            if b % 8 == 0:
                break
        # hint which is faster a & 0xffff == b & 0xffff
        if judge(a, b):
            matches += 1

    print('Second solution: {}'.format(matches))


if __name__ == "__main__":
    task1(289, 629)
    task2(289, 629)
    # test input
    # task1(65, 8921)
    # task2(65, 8921)
