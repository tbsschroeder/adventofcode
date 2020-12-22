from lib import get_input


def change_direction(orientation, direction, degree):
    current = 0
    if orientation == 'N':
        current = 0
    elif orientation == 'E':
        current = 1
    elif orientation == 'S':
        current = 2
    elif orientation == 'W':
        current = 3

    # summary for the if/else L/R
    tmp = degree if direction == 'R' else -degree
    current = (current + tmp / 90) % 4
    # if direction == 'L':
    #     if degree == 0:   current = (current - 0) % 4
    #     elif degree == 90:  current = (current - 1) % 4
    #     elif degree == 180: current = (current - 2) % 4
    #     elif degree == 270: current = (current - 3) % 4
    # if direction == 'R':
    #     if degree == 0:   current = (current + 0) % 4
    #     elif degree == 90:  current = (current + 1) % 4
    #     elif degree == 180: current = (current + 2) % 4
    #     elif degree == 270: current = (current + 3) % 4

    if current == 0:
        return 'N'
    elif current == 1:
        return 'E'
    elif current == 2:
        return 'S'
    elif current == 3:
        return 'W'


def move(action, value, north, east):
    if action == 'N':
        north += value
    if action == 'S':
        north -= value
    if action == 'E':
        east += value
    if action == 'W':
        east -= value
    return north, east


def part1():
    data = get_input('./input/input12.txt', '\n')
    instructions = [(line[0], int(line[1:])) for line in data]
    north = 0
    east = 0
    orientation = 'E'

    for (action, value) in instructions:
        if action in ['L', 'R']:
            orientation = change_direction(orientation, action, value)
            continue
        north, east = move(action, value, north, east)
        if action == 'F':
            north, east = move(orientation, value, north, east)

    print(abs(north) + abs(east))


def part2():
    data = get_input('./input/input12.txt', '\n')
    instructions = [(line[0], int(line[1:])) for line in data]

    card = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
    ship = 0, 0
    waypoint = 10, 1

    for (action, value) in instructions:
        if action in card:
            waypoint = waypoint[0] + value * card[action][0], \
                waypoint[1] + value * card[action][1]
        elif action == 'F':
            ship = ship[0] + value * waypoint[0], \
                ship[1] + value * waypoint[1]
        else:
            x, y = waypoint
            clockwise_degrees = {'L': 360 - value, 'R': value}[action]
            waypoint = {90: (y, -x),
                        180: (-x, -y),
                        270: (-y, x)}[clockwise_degrees]

    print(sum(map(abs, ship)))


if __name__ == "__main__":
    # iterative approach
    part1()
    # mapping approach
    part2()
