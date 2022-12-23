from lib import get_input
from operator import add, sub, mul, truediv

monkeys = {}
ops = {'+': add, '-': sub, '*': mul, '/': truediv}


def get_monkeys():
    for key, val in [line.split(': ') for line in get_input('./input/input21.txt', '\n')]:
        if bool([s for s in ['+', '-', '*', '/'] if (s in val)]):
            monkeys[key] = [val[:4], val[5:6], val[7:]]
        else:
            monkeys[key] = int(val)
    return monkeys


def calc_monkey(monkey):
    tmp = monkeys[monkey]
    if isinstance(tmp, int):
        return str(tmp)
    else:
        left = str(calc_monkey(tmp[0]))
        op = str(tmp[1])
        right = str(calc_monkey(tmp[2]))
        return eval(left + op + right)


def part1():
    get_monkeys()
    print(calc_monkey('root'))


class Node:
    def __init__(self, l):
        self.name = l[:4]
        self.raw = l[6:]
        self.val = None

    def eval(self):
        if self.val is None:
            return self.op(self.lhs.eval(), self.rhs.eval())
        else:
            return self.val


def buildTree(nodes, node='root'):
    n = nodes[node]
    raw = n.raw
    if raw[0] in '0123456789':
        n.val = int(raw)
    else:
        lhs, op, rhs = raw.split()
        n.lhs = nodes[lhs]
        n.rhs = nodes[rhs]
        n.op = ops[op]
        for t in (lhs, rhs):
            buildTree(nodes, t)


def part2():
    nodes = {}
    for line in get_input('./input/input21.txt', '\n'):
        n = Node(line)
        nodes[n.name] = n
    buildTree(nodes, 'root')

    nodes['humn'].val = 1j
    solve, const = nodes['root'].lhs.eval(), nodes['root'].rhs.eval()
    if const.imag:
        solve, const = const, solve
    p2 = int((const - solve.real) / solve.imag)

    print(p2)


if __name__ == "__main__":
    part1()
    part2()
