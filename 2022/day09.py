from lib import get_input


DELTA = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}


def sign(x):
    return (x > 0) - (x < 0)


def part1and2():
    lines = [line for line in get_input('./input/input09.txt', '\n')]

    rope = [(0, 0)] * 10
    seen1 = {(0, 0)}
    seen9 = {(0, 0)}

    for line in lines:
        direction, steps = line.split()
        steps = int(steps)

        for _ in range(steps):
            hx, hy = rope[0]
            dx, dy = DELTA[direction]
            rope[0] = hx + dx, hy + dy

            for i in range(9):
                hx, hy = rope[i]
                tx, ty = rope[i + 1]
                dx, dy = hx - tx, hy - ty

                if dx**2 + dy**2 >= 4:
                    rope[i + 1] = tx + sign(dx), ty + sign(dy)

            seen1.add(tuple(rope[1]))
            seen9.add(tuple(rope[9]))

    print(len(seen1), len(seen9))


if __name__ == "__main__":
    part1and2()
