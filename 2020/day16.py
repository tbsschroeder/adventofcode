from lib import get_input, get_raw_input
import re
from math import prod


def part1():
    raw_rules, _, nearby = get_input('./input/input16.txt', '\n\n')

    valid = []
    err = 0
    for line in raw_rules.split('\n'):
        _, rule = line.split(': ')
        no = rule.split(' ')
        val_range1 = int(no[0].split('-')[0])
        val_range2 = int(no[0].split('-')[1])
        val_range3 = int(no[2].split('-')[0])
        val_range4 = int(no[2].split('-')[1])
        valid += range(val_range1, val_range2 + 1)
        valid += range(val_range3, val_range4 + 1)
    for line in nearby.split('\n')[1:]:
        fields = line.split(',')
        for field in fields:
            if int(field) in valid:
                continue
            else:
                err += int(field)
    print(err)
    return valid


def parse_rules(raw_rules):
    rules = {}
    for rule in raw_rules.splitlines():
        m = re.match('(.*): (\d+)\-(\d+) or (\d+)\-(\d+)', rule)
        name = m.group(1)
        range_1 = range(int(m.group(2)), int(m.group(3))+1)
        range_2 = range(int(m.group(4)), int(m.group(5))+1)
        rules[name] = set(range_1) | set(range_2)
    return rules


def part2():
    raw_rules, raw_ticket, raw_nearby = get_input(
        './input/input16.txt', '\n\n')
    rules = parse_rules(raw_rules)
    my_ticket = list(map(int, raw_ticket.splitlines()[1].split(',')))
    nearby = [list(map(int, l.split(',')))
              for l in raw_nearby.splitlines()[1:]]

    nearby = [ticket for ticket in nearby
              if all(any(n in nums for nums in rules.values())
                     for n in ticket)]

    rule_order_candidates = []
    for vals in zip(*nearby):
        candidates = set()
        for name, valid_nums in rules.items():
            if all(v in valid_nums for v in vals):
                candidates.add(name)
        rule_order_candidates.append(candidates)

    rule_order = [None] * len(rule_order_candidates)
    for _ in range(len(rule_order)):
        for idx, candidates in enumerate(rule_order_candidates):
            if rule_order[idx] is None and 1 == len(candidates):
                (rule_order[idx],) = candidates
                for j, old_candidates in enumerate(rule_order_candidates):
                    rule_order_candidates[j] = old_candidates - candidates
                break
    assert(None not in rule_order)

    answer = 1
    for name, val in zip(rule_order, my_ticket):
        if name.startswith('departure'):
            answer *= val

    print(answer)


if __name__ == "__main__":
    part1()
    part2()
