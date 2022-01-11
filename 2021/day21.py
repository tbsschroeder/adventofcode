from lib import get_input


def part1(pos1, pos2):
    score1, score2 = 0, 0
    dice = [1, 2, 3]
    roll_dice = 0

    while score1 < 1000 and score2 < 1000:
        pos1 += sum(dice)
        score1 += pos1 % 10 if pos1 % 10 else 10
        dice, roll_dice = [(d + 3) % 100 for d in dice], roll_dice + 3
        if score1 >= 1000:
            break
        pos2 += sum(dice)
        score2 += pos2 % 10 if pos2 % 10 else 10
        dice, roll_dice = [(d + 3) % 100 for d in dice], roll_dice + 3
    print(score1 * roll_dice if score1 < score2 else score2 * roll_dice)


def split_universe(pos1, turn1, pos2, turn2):
    if turn2 <= 0:
        return (0, 1)

    wins1, wins2 = 0, 0
    for (r, f) in [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]:
        c2, c1 = split_universe(pos2, turn2, (pos1 + r) % 10, turn1 - 1 - (pos1 + r) % 10)
        wins1, wins2 = wins1 + f * c1, wins2 + f * c2

    return wins1, wins2


def part2():
    print(max(split_universe(pos1 - 1, 21, pos2 - 1, 21)))


if __name__ == "__main__":
    pos1, pos2 = [int(l.split(': ')[1]) for l in get_input('./input/input21.txt', '\n')]
    part1(pos1, pos2)
    part2()
