from lib import get_input


def extract_window(x, y, m):
    if (x, y) == (0, 0):
        return [m[x + 1][y], m[x][y + 1]]
    elif (x, y) == (len(m) - 1, len(m[0]) - 1):
        return [m[x - 1][y], m[x - 1][y - 1]]
    elif (x, y) == (0, len(m[0]) - 1):
        return [m[x][y - 1], m[x + 1][y]]
    elif y == len(m[0]) - 1:
        return [m[x - 1][y], m[x][y - 1], m[x + 1][y]]
    elif (x, y) == (len(m) - 1, 0):
        return [m[x - 1][y], m[x][y + 1]]
    elif x == len(m) - 1:
        return [m[x - 1][y], m[x][y - 1], m[x][y + 1]]
    elif x == 0:
        return [m[x][y - 1], m[x + 1][y], m[x][y + 1]]
    elif y == 0:
        return [m[x - 1][y], m[x + 1][y], m[x][y + 1]]

    return [m[x - 1][y], m[x][y - 1], m[x + 1][y], m[x][y + 1]]


def check(m, x, y, visited, r_len, c_len):
    if 0 in [x, y] or x > r_len or y > c_len or m[x][y] == 9 or (x, y) in visited:
        return

    visited.append((x, y))

    check(m, x, y + 1, visited, r_len, c_len)
    check(m, x, y - 1, visited, r_len, c_len)
    check(m, x - 1, y, visited, r_len, c_len)
    check(m, x + 1, y, visited, r_len, c_len)


def part1and2():
    data = [list(map(int, list(line.strip()))) for line in get_input('./input/input09.txt', '\n')]

    heights_sum = []
    for i in range(0, len(data)):
        for j in range(0, len(data[0])):
            cur = data[i][j]
            if cur < min(extract_window(i, j, data)):
                heights_sum.append((i, j, cur))

    print(sum(value + 1 for _, _, value in heights_sum))

    basins = []
    for heights in heights_sum:
        i, j, z = heights
        visited = []
        check(data, i, j, visited, len(data) - 1, len(data[0]) - 1)
        basins.append(len(visited))

    basins.sort(reverse=True)
    print(basins[0] * basins[1] * basins[2])


if __name__ == "__main__":
    part1and2()
