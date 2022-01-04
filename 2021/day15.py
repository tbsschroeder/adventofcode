from lib import get_input


def inr(pos, arr):
    return pos[0] in range(len(arr)) and pos[1] in range(len(arr[0]))


def do_dijkstra(data):
    mem = [(0, 0, 0)]
    costs = {}
    while True:
        cost, x, y = mem[0]
        if x == len(data) - 1 and y == len(data[0]) - 1:
            print(cost)
            break

        mem = mem[1:]
        for new_x, new_y in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]:
            if inr((new_x, new_y), data):
                nc = cost + data[new_x][new_y]
                if (new_x, new_y) in costs and costs[(new_x, new_y)] <= nc:
                    continue
                costs[(new_x, new_y)] = nc
                mem.append((nc, new_x, new_y))
        mem = sorted(mem)


def part1():
    data = [[int(y) for y in x] for x in get_input('./input/input15.txt', '\n')]
    do_dijkstra(data)


def part2():
    data = [[int(y) for y in x] for x in get_input('./input/input15.txt', '\n')]

    expanded = [[0 for _ in range(5 * len(data[0]))] for _ in range(5 * len(data))]

    for x in range(0, len(expanded)):
        for y in range(0, len(expanded[0])):
            dist = x // len(data) + y // len(data[0])
            new_val = data[x % len(data)][y % len(data[0])]
            for i in range(dist):
                new_val += 1
                if new_val == 10:
                    new_val = 1
            expanded[x][y] = new_val

    data = expanded

    do_dijkstra(data)


if __name__ == "__main__":
    part1()
    part2()
