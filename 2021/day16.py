import math


op = [sum, math.prod, min, max,
      lambda ls: ls[0],
      lambda ls: 1 if ls[0] > ls[1] else 0,
      lambda ls: 1 if ls[0] < ls[1] else 0,
      lambda ls: 1 if ls[0] == ls[1] else 0]


def hex2bin(char):
    return format(int(char, 16), '04b')


def part1(start_bit):
    i = start_bit

    version = int(my_bytes[i:i + 3], 2)
    type_id = int(my_bytes[i + 3:i + 6], 2)
    i += 6

    if type_id == 4:
        while True:
            i += 5
            if my_bytes[i - 5] == '0':
                break
    else:
        if my_bytes[i] == '0':
            j = i + 16 + int(my_bytes[i + 1:i + 16], 2)
            i += 16
            while i < j:
                i, v = part1(i)
                version += v
        else:
            np = int(my_bytes[i + 1:i + 12], 2)
            i += 12
            for _ in range(np):
                i, v = part1(i)
                version += v

    return i, version


def part2(start_bit):
    i = start_bit

    type_id = int(my_bytes[i + 3:i + 6], 2)
    i += 6

    if type_id == 4:
        vals = [0]
        while True:
            vals[0] = 16 * vals[0] + int(my_bytes[i + 1:i + 5], 2)
            i += 5
            if my_bytes[i - 5] == '0':
                break
    else:
        vals = []
        if my_bytes[i] == '0':
            j = i + 16 + int(my_bytes[i + 1:i + 16], 2)
            i += 16
            while i < j:
                i, v = part2(i)
                vals.append(v)
        else:
            np = int(my_bytes[i + 1:i + 12], 2)
            i += 12
            for _ in range(np):
                i, v = part2(i)
                vals.append(v)

    return i, op[type_id](vals)


if __name__ == "__main__":
    data = bin(int('1' + open('./input/input16.txt').read(), 16))
    my_bytes = data[3:]

    print(part1(0)[1])
    print(part2(0)[1])
