from lib import get_input


EAST = 'e'
SOUTHEAST = 'se'
SOUTHWEST = 'sw'
WEST = 'w'
NORTHEAST = 'ne'
NORTHWEST = 'nw'

directions = {
    EAST: (+2, 0),
    SOUTHEAST: (+1, -1),
    SOUTHWEST: (-1, -1),
    WEST: (-2, 0),
    NORTHEAST: (+1, +1),
    NORTHWEST: (-1, +1),
}


def get_tiles(data):
    tiles = []
    for line in data:
        tile = []
        ix = 0
        while ix < len(line):
            if line.startswith((EAST, WEST), ix):
                tile.append(line[ix])
                ix += 1
            else:
                tile.append(line[ix:ix+2])
                ix += 2
        tiles.append(tile)
    return tiles


def part1():
    data = get_input('./input/input24.txt', '\n')
    tiles = get_tiles(data)

    black_coord = set()

    for tile in tiles:
        coord = (0, 0)
        for i in tile:
            coord = (coord[0] + directions[i][0], coord[1] + directions[i][1])
        if coord in black_coord:
            black_coord.remove(coord)
        else:
            black_coord.add(coord)

    print(len(black_coord))
    return black_coord

def count_adjacent_black_tiles(coord, black_coord):
    return sum(
        1 if (coord[0] + d[0], coord[1] + d[1]) in black_coord else 0
        for d in directions.values()
    )

def part2():
    black_coord = part1()

    for _ in range(100):
        new_black_coord = set()

        min_x, max_x = float('inf'), float('-inf')
        min_y, max_y = float('inf'), float('-inf')
        for coord in black_coord:
            min_x, max_x = min(min_x, coord[0]), max(max_x, coord[0])
            min_y, max_y = min(min_y, coord[1]), max(max_y, coord[1])

        for j in range(min_x - 2, max_x + 2 + 1):
            for k in range(min_y - 1, max_y + 1 + 1):
                coord = (j, k)
                count = count_adjacent_black_tiles(coord, black_coord)

                if coord in black_coord:
                    if 0 < count <= 2:
                        new_black_coord.add(coord)
                elif count == 2:
                    new_black_coord.add(coord)

        black_coord = new_black_coord

    print(len(black_coord))


if __name__ == "__main__":
    part1()
    part2()
