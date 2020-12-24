from functools import reduce

input = 'nbysizxe'


def run_around(lengths, numbers, pos, skip_size):
    for i in lengths:
        tmp = numbers + numbers
        tmp[pos:pos + i] = tmp[pos:pos + i][::-1]
        if pos + i > len(numbers):
            numbers = tmp[len(numbers):pos + i] + tmp[pos + i - len(numbers):len(numbers)]
        else:
            numbers = tmp[:len(numbers)]
        pos = (pos + i + skip_size) % len(numbers)
        skip_size += 1
    return numbers, pos, skip_size


def knot_hash(ascii_length):
    ascii_length += [17, 31, 73, 47, 23]

    # rund around
    no_list = list(range(256))
    pos = 0
    skip_size = 0
    for runs in range(64):
        no_list, pos, skip_size = run_around(ascii_length, no_list, pos, skip_size)

    # create hash
    chunks = [no_list[x:x + 16] for x in range(0, len(no_list), 16)]
    dense_hash = [reduce(lambda i, j: int(i) ^ int(j), tmp) for tmp in chunks]

    hex_hash = [hex(dec).split('x')[-1] for dec in dense_hash]
    return hex_hash


def knot_hash_to_bin(hash):
    return ''.join([format(int(h, 16), '0>8b') for h in hash])


disk = []
for i in range(128):
    ascii_tmp = [ord(c) for c in '{}-{}'.format(input, i)]
    disk.append([int(h) for h in knot_hash_to_bin(knot_hash(ascii_tmp))])

used = sum([row.count(1) for row in disk])

print('First solution: {}'.format(used))

hash_rep = []
for d in disk:
    hash_rep.append([str(c).replace('1', '#').replace('0', '.') for c in d])

group_id = 0
neighbors = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def mark_it(group, x, y):
    if is_int(hash_rep[x][y]) or hash_rep[x][y] == '.':
        return

    hash_rep[x][y] = group
    for n in neighbors:
        if x + n[0] in range(128) and y + n[1] in range(128):
            mark_it(group, x + n[0], y + n[1])


for x in range(128):
    for y in range(128):
        if hash_rep[x][y] == '#':
            group_id += 1
            mark_it(group_id, x, y)

print('Second solution: {}'.format(group_id))
