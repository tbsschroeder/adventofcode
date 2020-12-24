from functools import reduce


def def_input():
    input = """187,254,0,81,169,219,1,190,19,102,255,56,46,32,2,216"""
    no_list = list(range(256))
    lengths = list(map(int, input.split(',')))
    pos = 0
    skip_size = 0
    return input, no_list, lengths, pos, skip_size


def def_test_input():
    test_input = """3,4,1,5"""
    test_no_list = list(range(5))
    test_lengths = list(map(int, test_input.split(',')))
    pos = 0
    skip_size = 0
    return test_input, test_no_list, test_lengths, pos, skip_size


def run_around(lengths, numbers, pos, skip_size):
    for i in lengths:
        tmp = numbers + numbers
        tmp[pos:pos + i] = tmp[pos:pos + i][::-1]
        if pos + i > len(numbers):
            numbers = tmp[len(numbers):pos + i] + tmp[pos + i - len(numbers):len(numbers)]
        else:
            numbers = tmp[:len(numbers)]

        # print('Lengths: {}, Pos: {},  Skip: {}, List: {}'.format(i, pos, skip_size, numbers))

        pos = (pos + i + skip_size) % len(numbers)
        skip_size += 1
    return numbers, pos, skip_size


input, no_list, lengths, pos, skip_size = def_input()
no_list, pos, skip_size = run_around(lengths, no_list, pos, skip_size)
print('First solution: {}'.format(no_list[0] * no_list[1]))

###

input, no_list, lengths, pos, skip_size = def_input()

# input = [1,2,3]
# input = [1,2,4]

# convert ascii
ascii_length = [ord(c) for c in input] + [17, 31, 73, 47, 23]

# rund around
for runs in range(64):
    no_list, pos, skip_size = run_around(ascii_length, no_list, pos, skip_size)

# create hash
chunks = [no_list[x:x + 16] for x in range(0, len(no_list), 16)]
dense_hash = [reduce(lambda i, j: int(i) ^ int(j), tmp) for tmp in chunks]

hex_hash = [hex(dec).split('x')[-1] for dec in dense_hash]

print('Second solution: {}'.format(''.join(hex_hash)))
