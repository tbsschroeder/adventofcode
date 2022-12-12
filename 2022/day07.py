from lib import get_input


def buildDirectories(d, data, prev):
    while data:
        cmd = data.pop(0)
        if cmd == '$ ls':
            while data and not data[0].startswith('$'):
                a, b = data.pop(0).split(' ')
                d[prev + (b,)] = {} if a == 'dir' else int(a)
        elif cmd.endswith('..'):
            return
        else:
            c = cmd.split(' ')[-1]
            p = prev + (c,)
            buildDirectories(d[p], data, prev + p)
    return d


def findTotalSpacePerDir(d, key):
    current_sum = 0
    for k, v in d.items():
        if isinstance(v, int):
            current_sum += v
        else:
            current_sum += findTotalSpacePerDir(v, k)
    totalSpace[key] = current_sum
    return current_sum


if __name__ == '__main__':
    data = get_input('./input/input07.txt', '\n')[1:]
    d = {'/': {}}
    directories = buildDirectories(d['/'], data, ('/',))
    totalSpace = {}

    findTotalSpacePerDir(directories, key='/')
    print(sum(v for v in totalSpace.values() if v <= 100000))

    needed_space = 70000000 - max(totalSpace.values())
    print(min([v for v in totalSpace.values() if v > 30000000 - needed_space]))
