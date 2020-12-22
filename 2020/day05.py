from lib import get_input


def get_row(code):
    return int(code.replace('F', '0').replace('B', '1'), 2)


def get_column(code):
    return int(code.replace('L', '0').replace('R', '1'), 2)


def part1():
    data = get_input('./input/input05.txt', '\n')
    seat_ids = [get_row(line[:7]) * 8 + get_column(line[7:]) for line in data]
    print(max(seat_ids))


def part2():
    data = get_input('./input/input05.txt', '\n')
    seats = {}
    for line in data:
        row = get_row(line[1:7])
        col = get_column(line[7:])
        if row in seats:
            seats[row].append(col)
        else:
            seats[row] = [col]
    for row in seats:
        diff = list(set(range(0, 8)) - set(seats[row]))
        if len(diff) > 0:
            print(row * 8 + diff[0])


if __name__ == "__main__":
    part1()
    part2()
