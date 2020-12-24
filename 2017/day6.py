from collections import OrderedDict

input = "10	3	15	10	5	15	5	15	9	2	5	8	5	2	3	6"

bank = list(map(int, input.split()))
seen_before = OrderedDict()

while tuple(bank) not in seen_before:
    seen_before[tuple(bank)] = len(seen_before)
    pos = bank.index(max(bank))
    tmp_max = bank[pos]
    bank[pos] = 0
    for i in range(1, tmp_max + 1):
        tmp = (pos + i) % len(bank)
        bank[tmp] += 1

print('First solution: {}'.format(len(seen_before)))

print('Second solution: {}'.format(len(seen_before) - seen_before[tuple(bank)]))
