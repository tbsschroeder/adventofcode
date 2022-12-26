from lib import get_input
from functools import reduce


def SNAFUtoDec(num):
    return reduce(
        lambda r, v: (
            r[0] + ("=-012".index(v) - 2)* r[1],
            r[1] * 5,
        ),
        num[::-1],
        (0, 1),
    )[0]

def decToSNAFU(num):
    res = []
    while num > 0:
        res.append("012=-"[num % 5])
        num = (2+num) // 5
    return ''.join(res[::-1])

if __name__ == "__main__":
    data = [line for line in get_input('./input/input25.txt', '\n')]
    print(decToSNAFU(sum(SNAFUtoDec(l) for l in data)))
