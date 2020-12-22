from lib import get_input
import itertools
import copy

Floor = '.'
Empty = 'L'
Occupied = '#'


def is_seat_reachable(seats, row, x, col, y):
    try:
        if row + x in range(0, len(seats)):
            if col + y in range(0, len(seats[row + x])):
                return seats[row + x][col + y] != Floor
    except IndexError:
        return False
    return False


def is_seat_far_away_reachable(seats, row, x, col, y):
    count = 1
    while is_seat_reachable(seats, row, count * x, col, count * y):
        if seats[row + count * x][col + count * y] == Floor:
            count += 1
    count -= 1
    return seats[row + count * x][col + count * y] != Floor


def rearrange_occupied(old_seats, new_seats, row, col, free_count, far_sight):
    occupied_seats = []
    prod = list(itertools.product([-1, 0, 1], repeat=2))
    prod.remove((0, 0))

    for (x, y) in prod:
        if not far_sight:
            if is_seat_reachable(old_seats, row, x, col, y):
                occupied_seats.append(old_seats[row + x][col + y] == Occupied)
        else:
            if is_seat_far_away_reachable(old_seats, row, x, col, y):
                occupied_seats.append(old_seats[row + x][col + y] == Occupied)

    if old_seats[row][col] == Empty and True not in occupied_seats:
        new_seats[row][col] = Occupied
    elif old_seats[row][col] == Occupied and occupied_seats.count(True) >= free_count:
        new_seats[row][col] = Empty


def seats_as_string(seats):
    return ''.join(list(itertools.chain.from_iterable(seats)))


def part1():
    seats = get_input('./input/input11.txt', '\n')
    for i, line in enumerate(seats):
        seats[i] = [c for c in line]

    old_seats = []
    new_seats = copy.deepcopy(seats)
    count = 0

    while seats_as_string(old_seats) != seats_as_string(new_seats):
        count += 1
        old_seats = copy.deepcopy(new_seats)
        for row in range(len(seats)):
            for col in range(len(new_seats[row])):
                rearrange_occupied(old_seats, new_seats, row, col, 4, False)
    print(seats_as_string(new_seats).count(Occupied))


def part2():
    seats = get_input('./input/input11.txt', '\n')
    for i, line in enumerate(seats):
        seats[i] = [c for c in line]

    old_seats = []
    new_seats = copy.deepcopy(seats)
    count = 0

    while seats_as_string(old_seats) != seats_as_string(new_seats):
        count += 1
        old_seats = copy.deepcopy(new_seats)
        for row in range(len(seats)):
            for col in range(len(new_seats[row])):
                rearrange_occupied(old_seats, new_seats, row, col, 5, True)
    print(seats_as_string(new_seats).count(Occupied))


if __name__ == "__main__":
    part1()
    part2()
