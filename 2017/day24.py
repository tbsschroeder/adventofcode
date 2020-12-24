input = """42/37
    28/28
    29/25
    45/8
    35/23
    49/20
    44/4
    15/33
    14/19
    31/44
    39/14
    25/17
    34/34
    38/42
    8/42
    15/28
    0/7
    49/12
    18/36
    45/45
    28/7
    30/43
    23/41
    0/35
    18/9
    3/31
    20/31
    10/40
    0/22
    1/23
    20/47
    38/36
    15/8
    34/32
    30/30
    30/44
    19/28
    46/15
    34/50
    40/20
    27/39
    3/14
    43/45
    50/42
    1/33
    6/39
    46/44
    22/35
    15/20
    43/31
    23/23
    19/27
    47/15
    43/43
    25/36
    26/38
    1/10"""

test_input = """0/2
    2/2
    2/3
    3/4
    3/5
    0/1
    10/1
    9/10"""

bridges = list(map(lambda x: tuple(map(int, x.strip().split('/'))), input.split('\n')))


def dfs_rec(start_port, curr_bridges, left_bridges):
    valid_bridges = [b for b in left_bridges if start_port in b]
    if len(valid_bridges) == 0:
        yield curr_bridges

    for bridge in valid_bridges:
        next_port = bridge[0] if bridge[1] == start_port else bridge[1]
        left_bridges.remove(bridge)
        curr_bridges.append(bridge)
        yield from dfs_rec(next_port, curr_bridges, left_bridges)
        left_bridges.append(bridge)
        curr_bridges.remove(bridge)


infos = []
for start in [b for b in bridges if 0 in b]:
    next_port = start[0] if start[1] == 0 else start[1]
    valids = [br for br in bridges if br is not start]
    for b in dfs_rec(next_port, [start], valids):
        infos.append({'length': len(b),
                      'sum': sum([x + y for x, y in b]),
                      'data': list(b)
                      })

max_s = max(infos, key=lambda x: x['sum'])
max_l = max(infos, key=lambda x: x['length'])
max_infos = [b for b in infos if len(b['data']) == max_l['length']]
max_l = max(max_infos, key=lambda x: x['sum'])

print('First solution: {}'.format(max_s['sum']))
print('Second solution: {}'.format(max_l['sum']))
