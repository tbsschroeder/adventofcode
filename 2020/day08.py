from lib import get_input


def run(data):
    acc = 0
    exec_index = []
    next_index = 0
    while next_index not in exec_index and next_index < len(data):
        exec_index.append(next_index)
        cmd, val = data[next_index].split(' ')
        if cmd == 'nop':
            next_index += 1
        if cmd == 'acc':
            acc += int(val)
            next_index += 1
        if cmd == 'jmp':
            next_index += int(val)
    return acc, next_index in exec_index


def part1():
    data = get_input('./input/input08.txt', '\n')
    acc, _ = run(data)
    print(acc)


def change_cmd(index, data):
    new_data = data.copy()
    while index < len(data):
        index += 1
        if 'jmp' in new_data[index]:
            new_data[index] = new_data[index].replace('jmp', 'nop')
            return index, new_data
        if 'nop' in new_data[index]:
            new_data[index] = new_data[index].replace('nop', 'jmp')
            return index, new_data


def part2():
    data = get_input('./input/input08.txt', '\n')
    infinite_loop = True
    index = -1
    acc = 0
    while infinite_loop:
        index, edit_data = change_cmd(index, data)
        acc, infinite_loop = run(edit_data)
    print(acc)


if __name__ == "__main__":
    part1()
    part2()
