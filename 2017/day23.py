input = """set b 67
    set c b
    jnz a 2
    jnz 1 5
    mul b 100
    sub b -100000
    set c b
    sub c -17000
    set f 1
    set d 2
    set e 2 <---
    set g d
    mul g e
    sub g b
    jnz g 2
    set f 0
    sub e -1
    set g e
    sub g b
    jnz g -8
    sub d -1
    set g d
    sub g b
    jnz g -13
    jnz f 2
    sub h -1
    set g b
    sub g c
    jnz g 2
    jnz 1 3
    sub b -17
    jnz 1 -23"""

instructions = list(map(str.strip, input.split('\n')))


def work():
    regs = {chr(97 + i): 0 for i in range(8)}
    # regs['a'] = 1

    def val(v):
        try:
            return int(v)
        except ValueError:
            return regs[v]

    i = 0
    count = 0

    while 0 <= i < len(instructions) - 1:

        cmd = instructions[i].split()
        # print('{} {} {}'.format(i, cmd, regs))

        if cmd[0] == 'set':
            regs[cmd[1]] = val(cmd[2])
        elif cmd[0] == 'sub':
            regs[cmd[1]] -= val(cmd[2])
        elif cmd[0] == 'mul':
            regs[cmd[1]] *= val(cmd[2])
            count += 1
        if cmd[0] == 'jnz' and (val(cmd[1]) != 0):
                i += val(cmd[2])
        else:
            i += 1
    return count


def debug():
    # reverse engineering after having a close look on the two nested loops
    # simply translate assembler to python and refactor that stuff
    tmp_b = 67 * 100 + 100000
    tmp_c = tmp_b + 17000
    sub_b = 17
    h = 0

    for b in range(tmp_b, tmp_c + 1, sub_b):
        for e in range(2, b):
            if b % e == 0:
                h += 1
                break

    return h


print('First solution: {}'.format(work()))
print('Second solution: {}'.format(debug()))
