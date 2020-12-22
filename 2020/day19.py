from lib import get_input


def parse_rules(raw_rules):
    rules = {}
    for line in raw_rules.split("\n"):
        no, rule = line.split(': ')
        if "|" in rule:
            rules[int(no)] = [[int(r) for r in t.split()]
                              for t in rule.split("|")]
        elif "\"" in line:
            rules[int(no)] = rule
        else:
            rules[int(no)] = [[int(r) for r in rule.split()]]
    return rules


def test_rule(word, seq, rules):
    if word == "" or seq == []:
        return word == "" and seq == []
    rule = rules[seq[0]]
    if "\"" in rule:
        return test_rule(word[1:], seq[1:], rules) if word[0] in rule else False
    else:
        return any(test_rule(word, r + seq[1:], rules) for r in rule)


def part1():
    raw_rules, words = get_input('./input/input19.txt', '\n\n')
    rules = parse_rules(raw_rules)
    words = [w for w in words.split("\n")]

    print(sum(test_rule(w, [0], rules) for w in words))


def part2():
    raw_rules, words = get_input('./input/input19.txt', '\n\n')
    raw_rules += "\n8: 42 | 42 8\n11: 42 31 | 42 11 31"
    rules = parse_rules(raw_rules)
    words = [w for w in words.split("\n")]

    print(sum(test_rule(w, [0], rules) for w in words))


if __name__ == "__main__":
    part1()
    part2()
