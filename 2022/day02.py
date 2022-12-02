from lib import get_input


def part1():
    strategy = {
        'A X': 4,  # Rock -     Rock      1 and draw 3
        'A Y': 8,  # Rock -     Paper     2 and win  6
        'A Z': 3,  # Rock -     Scissor   3 and loss 0
        'B X': 1,  # Paper -    Rock      1 and loss 0
        'B Y': 5,  # Paper -    Paper     2 and draw 3
        'B Z': 9,  # Paper -    Scissor   3 and win  6
        'C X': 7,  # Scissors - Rock      1 and win  6
        'C Y': 2,  # Scissors - Paper     2 and loss 0
        'C Z': 6,  # Scissors - Scissor   3 and draw 3
    }
    print(sum([strategy[line] for line in get_input('./input/input02.txt', '\n')]))


def part2():
    strategy = {
        'A X': 3,  # Rock -     loss -> scissor  3 and 0
        'A Y': 4,  # Rock -     draw -> rock     1 and 3
        'A Z': 8,  # Rock -     win ->  paper    2 and 6
        'B X': 1,  # Paper -    loss -> rock     1 and 0
        'B Y': 5,  # Paper -    draw -> paper    2 and 3
        'B Z': 9,  # Paper -    win ->  scissor  3 and 6
        'C X': 2,  # Scissors - loss -> paper    2 and 0
        'C Y': 6,  # Scissors - draw -> scissor  3 and 3
        'C Z': 7,  # Scissors - win ->  rock     1 and 6
    }
    print(sum([strategy[line] for line in get_input('./input/input02.txt', '\n')]))


if __name__ == "__main__":
    part1()
    part2()
