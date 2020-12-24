input = 347991

# calc sizes of the spirals
length = 1
round = 1
size = length * length

while size < input:
    length += 2
    round += 1
    size = length * length
    ring_start = (length - 2) * (length - 2) + 1
    ring_end = length * length

# get side of inputno
ring_start = ring_start - 1
while ring_start + length - 1 < input:
    ring_start += length - 1

# from input to mid
mid = int(length / 2) + ring_start
diff = abs(input - mid)

print('First solution: {}'.format(diff + round - 1))


def get_loc(i, j):
    return spirals[(i, j)] if (i, j) in spirals else 0


def turn_ccw(dx, dy):
    return [-dy, dx]


spirals = {}  # maps tuple (i,j) to a value
spirals[(0, 0)] = 1  # init
[dx, dy] = [1, 0]  # point right
[x, y] = [0, 0]  # start at origin
traveled_dist = 1
traveled = 0
increase_traveled_dist = False
while(spirals[(x, y)] < input):
    x += dx
    y += dy

    spirals[(x, y)] = (
        get_loc(x + 1, y + 1) +
        get_loc(x, y + 1) +
        get_loc(x - 1, y + 1) +
        get_loc(x + 1, y) +
        get_loc(x - 1, y) +
        get_loc(x + 1, y - 1) +
        get_loc(x, y - 1) +
        get_loc(x - 1, y - 1)
    )

    traveled += 1
    if (traveled == traveled_dist):
        traveled = 0
        [dx, dy] = turn_ccw(dx, dy)
        if (increase_traveled_dist):
            traveled_dist += 1
            increase_traveled_dist = False
        else:
            increase_traveled_dist = True

print('Second solution: {}'.format(spirals[x, y]))
