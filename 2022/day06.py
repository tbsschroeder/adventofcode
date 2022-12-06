from lib import get_input


def part1and2(datastream, seq):
    for pos in range(len(datastream) - seq):
        if len(set(datastream[pos:pos + seq])) == seq:
            print(pos + seq)
            break


if __name__ == "__main__":
    datastream = get_input('./input/input06.txt', '\n')[0]
    part1and2(datastream, 4)
    part1and2(datastream, 14)
