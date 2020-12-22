from lib import get_input
import re


def traverse_bag_lists(colors, col_set, bags_list, count):
    for bags in bags_list:
        if colors[0] in bags[1]:
            colors.append(bags[0])
            col_set = set(list(col_set) + list(bags[1]))

    colors.remove(colors[0])

    if len(colors) > 0:
        print(len(col_set))
        traverse_bag_lists(colors, col_set, bags_list, len(col_set))

    return max(len(col_set), count)


def part2(bags, parent):
    total = 1
    for child, number in bags[parent].items():
        total += int(number) * part2(bags, child)
    return total


def part1(bags, target, parents=set()):
    for key, value in bags.items():
        if target in value and key not in parents:
            parents.add(key)
            part1(bags, key, parents)

    return len(parents)


def prep_input(target):
    bags = dict()
    bags[target] = dict()

    data = get_input('./input/input07.txt', '\n')
    for line in data:
        parent, children = re.match(r'(.+?)s? contain (.+)', line).groups()
        children = re.findall(r'(\d) ([ a-z]+bag)?', children)

        if parent not in bags:
            bags[parent] = dict()

        for number, child in children:
            bags[parent][child] = number
    return bags


if __name__ == "__main__":
    target = 'shiny gold bag'
    bags = prep_input(target)

    print(part1(bags, target))
    print(part2(bags, target) - 1)
