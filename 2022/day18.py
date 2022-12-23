from lib import get_input
from itertools import combinations


def are_neighbors(a, b):
    return sum(abs(d1 - d2) for d1, d2 in zip(a, b)) == 1


def get_neighbors(point, minv, maxv):
    candidates = set()
    for delta in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
        new_point = tuple([d + offset for d, offset in zip(point, delta)])
        if not all([d >= minv and d <= maxv for d in new_point]):
            continue
        candidates.add(new_point)
    return candidates


def solve():
    puzzle = [tuple(map(int, line.split(','))) for line in get_input('./input/input18.txt', '\n')]
    part1 = 6 * len(puzzle)
    for a, b in combinations(puzzle, 2):
        if not are_neighbors(a, b):
            continue
        part1 -= 2

    part2 = 0
    puzzle = set(puzzle)
    minv = min(min(point) for point in puzzle) - 1
    maxv = max(max(point) for point in puzzle) + 1
    nodes = [(minv, minv, minv)]
    visited = {nodes[0]}
    while nodes:
        node = nodes.pop()
        for neighbor in get_neighbors(node, minv, maxv):
            if neighbor in visited:
                continue
            if neighbor in puzzle:
                part2 += 1
            else:
                visited.add(neighbor)
                nodes.append(neighbor)

    print(part1, part2)


if __name__ == "__main__":
    solve()
