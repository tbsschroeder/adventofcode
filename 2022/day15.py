from lib import get_input


def get_coords():
    data = [line.strip() for line in get_input('./input/input15.txt', '\n')]

    coords = []
    for line in data:
        l = (
            line.replace("Sensor at ", "")
            .replace(": closest beacon is at ", " ")
            .replace(",", "")
            .replace("x=", "")
            .replace("y=", "")
            .split()
        )
        coords.append((int(l[0]), int(l[1]), int(l[2]), int(l[3])))
    return coords


def part1(sensor_grid):
    row = 2000000
    no_beacon_set = set()
    for (x, y, u, v) in sensor_grid:
        sensor_x = x
        sensor_y = y
        distance = abs(x - u) + abs(y - v)
        remaining_distance = distance - abs(row - sensor_y)
        if remaining_distance < 0:
            continue
        if (sensor_x, row) != (u, v):
            no_beacon_set.add(sensor_x)
        for i in range(1, remaining_distance + 1):
            if (sensor_x - i, row) != (u, v):
                no_beacon_set.add(sensor_x - i)
        for i in range(1, remaining_distance + 1):
            if (sensor_x + i, row) != (u, v):
                no_beacon_set.add(sensor_x + i)
    print(len(no_beacon_set))


def merge_ranges(ranges):
    ranges.sort(key=lambda x: x[0])
    merged_ranges = []
    for i in range(len(ranges) - 1):
        r1 = ranges[i]
        r2 = ranges[i + 1]
        if r2[0] <= r1[1] <= r2[1] or r2[0] == r1[1] + 1:
            ranges[i + 1] = [r1[0], r2[1]]
        elif r1[0] <= r2[0] and r1[1] >= r2[1]:
            ranges[i + 1] = r1
            continue
        else:
            merged_ranges.append(r1)
    merged_ranges.append(ranges[-1])
    return merged_ranges


def part2(sensor_grid):
    for row in range(4000001):
        no_beacon_list = []
        for (x, y, u, v) in sensor_grid:
            sensor_x = x
            sensor_y = y
            distance = abs(x, u) + abs(y, v)
            remaining_distance = distance - abs(row - sensor_y)
            if remaining_distance < 0:
                continue
            no_beacon_list.append(
                [sensor_x - remaining_distance, sensor_x + remaining_distance]
            )
        no_beacon_ranges = merge_ranges(no_beacon_list)
        if len(no_beacon_ranges) > 1:
            print(4000000 * (no_beacon_ranges[0][1] + 1) + row)


if __name__ == "__main__":
    coords = get_coords()
    part1(coords)
    part2(coords)
