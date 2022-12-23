from lib import get_input
from collections import deque


def part1and2(part2=False):
    data = list(enumerate([int(x) * (811589153 if part2 else 1) for x in get_input('./input/input20.txt', '\n')]))
    mixed = deque(data[:])
    l = len(data)

    for _ in range(10 if part2 else 1):
        for p in data:
            i = mixed.index(p)
            mixed.rotate(-i)
            v = mixed.popleft()
            mixed.rotate(-v[1])
            mixed.appendleft(v)

    r = [x[1] for x in mixed]
    z = r.index(0)
    print(sum([r[(z + i) % l]for i in [1000, 2000, 3000]]))


if __name__ == "__main__":
    part1and2()
    part1and2(True)
