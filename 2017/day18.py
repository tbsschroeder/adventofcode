import multiprocessing.pool
import collections

input = """set i 31
    set a 1
    mul p 17
    jgz p p
    mul a 2
    add i -1
    jgz i -2
    add a -1
    set i 127
    set p 618
    mul p 8505
    mod p a
    mul p 129749
    add p 12345
    mod p a
    set b p
    mod b 10000
    snd b
    add i -1
    jgz i -9
    jgz a 3
    rcv b
    jgz b -1
    set f 0
    set i 126
    rcv a
    rcv b
    set p a
    mul p -1
    add p b
    jgz p 4
    snd a
    set a b
    jgz 1 3
    snd b
    set f 1
    add i -1
    jgz i -11
    snd a
    jgz f -16
    jgz a -19"""

test_input = """set a 1
    add a 2
    mul a a
    mod a 5
    snd a
    set a 0
    rcv a
    jgz a -1
    set a 1
    jgz a -2"""

instructions = list(map(str.strip, input.split('\n')))


def work(ident, inq, outq):
    regs = collections.defaultdict(int)
    regs['p'] = ident

    def val(v):
        try:
            return int(v)
        except ValueError:
            return regs[v]

    i = 0
    count = 0
    sound = None

    while 0 <= i < len(instructions) - 1:

        cmd = instructions[i].split()

        if cmd[0] == 'snd':
            sound = val(cmd[1])
            if outq:
                outq.put(val(cmd[1]))
            count += 1
        elif cmd[0] == 'set':
            regs[cmd[1]] = val(cmd[2])
        elif cmd[0] == 'add':
            regs[cmd[1]] += val(cmd[2])
        elif cmd[0] == 'mul':
            regs[cmd[1]] *= val(cmd[2])
        elif cmd[0] == 'mod':
            regs[cmd[1]] %= val(cmd[2])
        elif cmd[0] == 'rcv':
            if inq:
                regs[cmd[1]] = inq.get()
            elif regs[cmd[1]] != 0:
                return sound
        elif cmd[0] == 'jgz':
            if val(cmd[1]) > 0:
                i += val(cmd[2])
                continue
        i += 1

    return count


print('First solution: {}'.format(work(0, None, None)))

pool = multiprocessing.pool.ThreadPool(processes=2)

q1 = multiprocessing.Queue()
q2 = multiprocessing.Queue()

res1 = pool.apply_async(work, (0, q1, q2))
res2 = pool.apply_async(work, (1, q2, q1))

res1.get()
print('Second solution: {}'.format(res2.get()))
