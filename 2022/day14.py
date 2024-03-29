from lib import get_input


def cmp(x, y):
    return (x > y) - (x < y)


def get_rocks():
    shapes = [el.split(' -> ') for el in get_input('./input/input14.txt', '\n')]
    rocks = set()
    for points in shapes:
        points = [tuple(map(int, point.split(','))) for point in points]
        for i in range(1, len(points)):
            prev, curr = points[i - 1], points[i]
            dx, dy = cmp(curr[0], prev[0]), cmp(curr[1], prev[1])
            x, y = prev
            while (x, y) != curr:
                rocks.add((x, y))
                x, y = x + dx, y + dy
            rocks.add((x, y))
    return rocks


def get_next_sand_position(rocks, sand, floor):
    def _available(x, y):
        return (x, y) not in rocks and (x, y) not in sand and y < floor
    prevx = prevy = -1
    x, y = 500, 0
    while (prevx, prevy) != (x, y):
        prevx, prevy = x, y
        for dx, dy in [(0, 1), (-1, 1), (1, 1)]:
            if _available(x + dx, y + dy):
                x, y = x + dx, y + dy
                break
    return x, y


def fill_sand(rocks, floor, target_y):
    sand = set()
    position = get_next_sand_position(rocks, sand, floor)
    while position[1] != target_y:
        sand.add(position)
        position = get_next_sand_position(rocks, sand, floor)
    return len(sand)


if __name__ == "__main__":
    rocks = get_rocks()
    maxy = max(y for _, y in rocks)
    print(fill_sand(rocks, maxy + 1, maxy))
    print(fill_sand(rocks, maxy + 2, 0) + 1)
