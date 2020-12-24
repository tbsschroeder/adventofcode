tape = [0] * 100000
cursor = 100000 // 2
state = 'A'


for _ in range(12317297):
    if state == 'A':
        if tape[cursor] == 0:
            tape[cursor] = 1.
            cursor += 1
            state = 'B'
        else:
            tape[cursor] = 0
            cursor -= 1
            state = 'D'
    elif state == 'B':
        if tape[cursor] == 0:
            tape[cursor] = 1.
            cursor += 1
            state = 'C'
        else:
            tape[cursor] = 0
            cursor += 1
            state = 'F'
    elif state == 'C':
        if tape[cursor] == 0:
            tape[cursor] = 1.
            cursor -= 1
            state = 'C'
        else:
            tape[cursor] = 1
            cursor -= 1
            state = 'A'
    elif state == 'D':
        if tape[cursor] == 0:
            tape[cursor] = 0.
            cursor -= 1
            state = 'E'
        else:
            tape[cursor] = 1
            cursor += 1
            state = 'A'
    elif state == 'E':
        if tape[cursor] == 0:
            tape[cursor] = 1.
            cursor -= 1
            state = 'A'
        else:
            tape[cursor] = 0
            cursor += 1
            state = 'B'
    elif state == 'F':
        if tape[cursor] == 0:
            tape[cursor] = 0.
            cursor += 1
            state = 'C'
        else:
            tape[cursor] = 0
            cursor += 1
            state = 'E'

print('First solution: {}'.format(tape.count(1)))
