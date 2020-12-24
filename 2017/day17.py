inp = 343
buf = [0]
pos = 0

for i in range(1, 2017 + 1):
    pos = ((pos + inp) % len(buf)) + 1
    buf.insert(pos, i)

print('First solution: {}'.format(buf[buf.index(2017) + 1]))

buf = [0]
pos = 0
val_0 = 0

for i in range(1, 50000000 + 1):
    pos = (pos + inp) % i + 1

    if pos == 1:
        val_0 = i

print('Second solution: {}'.format(val_0))
