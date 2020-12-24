from operator import methodcaller

input = """0: 3
    1: 2
    2: 6
    4: 4
    6: 4
    8: 8
    10: 6
    12: 8
    14: 5
    16: 6
    18: 8
    20: 8
    22: 12
    24: 6
    26: 9
    28: 8
    30: 12
    32: 12
    34: 17
    36: 12
    38: 8
    40: 12
    42: 12
    44: 10
    46: 12
    48: 12
    50: 12
    52: 14
    54: 14
    56: 10
    58: 14
    60: 12
    62: 14
    64: 14
    66: 14
    68: 14
    70: 14
    72: 14
    74: 14
    76: 14
    86: 14
    94: 20
    96: 18"""

# input = """0: 3
#    1: 2
#    4: 4
#    6: 4"""

input = list(map(methodcaller('split', ': '), input.split('\n')))
depth_range = {int(l[0]): int(l[1]) for l in input}

firewall_positions = [-1] * (max(depth_range.keys()) + 1)
for step in depth_range:
    firewall_positions[step] = step % (depth_range[step] * 2 - 2)
busted = [i for i, x in enumerate(firewall_positions) if x == 0]

print('First solution: {}'.format(sum([depth_range[b] * b for b in busted])))

delay = -1
firewall_positions = [0] * (max(depth_range.keys()) + 1)

ranges = {step: (depth_range[step] * 2 - 2) for step in depth_range}


def busted(delay):
    for step in depth_range:
        if (delay + step) % ranges[step] == 0:
            return True
    return False


delay = 0
while busted(delay):
    delay += 1

print('Second solution: {}'.format(delay))
