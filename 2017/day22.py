input = """.#.##..##...#...#.....##.
#.......###..#...#.#.....
##.###..#....#.##.###.##.
##...#.#.##..#.#.###.....
.#....#..#..#..#..#...###
##.####....#...#...###...
#.#########.####...##..##
...###....#.##..##.#...##
##.###....#...#.##.######
.#.##.###.#.#..####..#..#
###.....##..##.##.#.#...#
....#.##.#.#.####.#...#..
....#...#..#...######.##.
##........###.###..#####.
....#.#.#..#######...##..
###.....####..#..##..####
#...##.#....####..##.#...
.##.#.#.....#.#.#..##..##
.#.#.#.##...##.###...####
.#..#.#...#......#...#..#
##.....##...#..####...###
..#####.#..###...#.#.#..#
.####.#....##..##...##..#
#.##..#.##..#.#.##..#...#
##.###.#.##########.#####"""

test_input = """.........
.........
.........
.....#...
...#.....
.........
.........
........."""

# healthy
to_left = {
    (1, 0): (0, 1),  # down to right
    (0, 1): (-1, 0),  # right to up
    (-1, 0): (0, -1),  # up to left
    (0, -1): (1, 0)  # left to down
}

# infected
to_right = {
    (1, 0): (0, -1),  # down to left
    (0, -1): (-1, 0),  # left to up
    (-1, 0): (0, 1),  # up to right
    (0, 1): (1, 0),  # right to down
}

# node status
status = {
    '.': 'W',
    'W': '#',
    '#': 'F',
    'F': '.'
}


def init(no, inp):
    grid = [[c for c in lines] for lines in inp.split('\n')]
    for _ in range(no):
        grid.insert(0, ['.'] * len(grid[0]))
        grid.append(['.'] * len(grid[0]))
        [row.insert(0, '.') for row in grid]
        [row.append('.') for row in grid]
        d = (-1, 0)  # up
        pos = (len(grid) // 2, len(grid[0]) // 2)  # middle
    return grid, d, pos


def new_dir(old_d, node):
    if node == '.':  # clean is left
        return to_left[old_d]
    elif node == '#':  # infected is right
        return to_right[old_d]
    elif node == 'F':  # flagged is reverse
        return (-old_d[0], -old_d[1])
    elif node == 'W':  # else nothing
        return old_d
    else:
        print('ERROR')


# task 1
grid, d, pos = init(200, input)
b = 0
for _ in range(10000):
    node = grid[pos[0]][pos[1]]
    d = to_right[d] if node == '#' else to_left[d]
    if node == '.':  # . gets to #
        b += 1
    grid[pos[0]][pos[1]] = '#' if node == '.' else '.'
    pos = (pos[0] + d[0], pos[1] + d[1])

print('First solution: {}'.format(b))

# tasl 2
grid, d, pos = init(250, input)
b = 0
for i in range(10000000):
    node = grid[pos[0]][pos[1]]
    d = new_dir(d, node)
    if node == 'W':  # W gets to #
        b += 1
    grid[pos[0]][pos[1]] = status[node]
    pos = (pos[0] + d[0], pos[1] + d[1])

print('Second solution: {}'.format(b))
