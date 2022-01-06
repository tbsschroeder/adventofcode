from lib import get_input


def part1():
    data = get_input('./input/input17.txt', '\n')[0]
    y_min, y_max = [int(y) for y in data.split(', ')[1].split('=')[1].split('..')]
    print((y_min + 1) * y_min // 2)


def part2():
    data = get_input('./input/input17.txt', '\n')[0]
    x_min, x_max = [int(x) for x in data.split(', ')[0].split('=')[1].split('..')]
    y_min, y_max = [int(y) for y in data.split(', ')[1].split('=')[1].split('..')]

    v = 0
    n = int((x_min * 2) ** 0.5 - 1)
    for dy_init in range(y_min, -y_min):
        for dx_init in range(n, x_max + 1):
            x = 0
            y = 0
            dx = dx_init
            dy = dy_init
            while x <= x_max and y >= y_min and (dx == 0 and x_min <= x or dx != 0):
                x += dx
                y += dy
                dx -= 1 if dx > 0 else 0
                dy -= 1
                if x in range(x_min, x_max + 1) and y in range(y_min, y_max + 1):
                    v += 1
                    break

    print(v)


if __name__ == "__main__":
    part1()
    part2()
