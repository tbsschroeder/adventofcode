from lib import get_input
from functools import partial, reduce
from itertools import product


def apply_mask(mask: str, number: int) -> int:
    number = list("{:0>36b}".format(int(number)))
    for index, bit in enumerate(list(mask)):
        if bit == '1':
            number[index] = '1'
        if bit == '0':
            number[index] = '0'
    return int(''.join(number), 2)


def part1():
    data = get_input('./input/input14.txt', '\n')
    mask = ''
    memory = {}
    for line in data:
        if line.startswith('mask'):
            mask = line.replace('mask = ', '')
            continue
        addr, value = line.replace('mem[', '').split('] = ')
        value = apply_mask(mask, int(value))
        memory[addr] = value
    print(sum(memory.values()))


def part2():
    data = get_input('./input/input14.txt', '\n')
    mask = ''
    memory = {}

    for line in data:
        if line.startswith('mask'):
            mask = line.replace('mask = ', '')
            continue

        qbits = []
        addr, value = line.replace('mem[', '').split('] = ')

        bin_addr = list(bin(int(addr))[2:])
        value = int(value)

        while len(bin_addr) < len(mask):
            bin_addr.insert(0, '0')

        for i, bit in enumerate(mask):
            if bit == '0':
                continue
            bin_addr[i] = bit
            if bit == 'X':
                qbits.append(i)

        combos = list(product([0, 1], repeat=len(qbits)))

        for combo in combos:
            for i in range(len(combo)):
                bin_addr[qbits[i]] = str(combo[i])
            new_addr = int(''.join(bin_addr), 2)
            memory[new_addr] = value

    print(reduce(lambda x, y: x+y, memory.values()))


if __name__ == "__main__":
    part1()
    part2()
