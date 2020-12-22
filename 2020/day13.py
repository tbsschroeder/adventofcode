from lib import get_input
from math import ceil
from functools import reduce


def part1():
    data = get_input('./input/input13.txt', '\n')
    timestamp, bus_ids = int(data[0]), [int(x)
                                        for x in data[1].split(',') if x != 'x']
    etas = {x: ceil(timestamp / x) * x for x in bus_ids}
    waiting_time = min(etas.values()) - timestamp
    bus_id = next((bus for bus, time in etas.items()
                   if time == min(etas.values())), None)
    print(waiting_time * bus_id)


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


# iterative and very slow approach
def part2():
    data = get_input('./input/input13.txt', '\n')
    offsets = [(int(bus), i)
               for i, bus in enumerate(data[1].split(',')) if bus != 'x']

    timestamp = 0
    while True:
        matching = []
        for (bus, count) in offsets[1:]:
            matching.append((timestamp + count) % bus == 0)

        if all(matching):
            break
        timestamp += offsets[0][0]
    print(timestamp)


def part2_fast():
    data = get_input('./input/input13.txt', '\n')
    buses = [(int(bus), i)
             for i, bus in enumerate(data[1].split(',')) if bus != 'x']
    dividers = [bus for bus, _ in buses]
    remainders = [bus - i for bus, i in buses]
    print(chinese_remainder(dividers, remainders))


if __name__ == "__main__":
    part1()
    # Google and the lowest common denominator of enumeration with offsets help ;)
    part2_fast()
    # part2()
