from lib import get_input


def calculate_score(deck) -> int:
    return sum([i * p for i, p in enumerate(deck[::-1], 1)])


def play_combat(deck1: list, deck2: list) -> int:
    while len(deck1) > 0 and len(deck2) > 0:
        if deck1[0] > deck2[0]:
            deck1 += [deck1[0], deck2[0]]
        else:
            deck2 += [deck2[0], deck1[0]]
        deck1.pop(0)
        deck2.pop(0)
    return calculate_score(deck1) if len(deck1) > 0 else 0 - calculate_score(deck2)


def play_recursive_combat(deck1: list, deck2: list) -> int:
    already_played = set()
    while len(deck1) > 0 and len(deck2) > 0:
        decks = (calculate_score(deck1), calculate_score(deck2))
        if decks in already_played:
            return(calculate_score(deck1))

        already_played.add(decks)
        card1 = deck1[0]
        card2 = deck2[0]
        deck1.pop(0)
        deck2.pop(0)
        if card1 <= len(deck1) and card2 <= len(deck2):
            if play_recursive_combat(deck1[:card1], deck2[:card2]) > 0:
                deck1 += [card1, card2]
            else:
                deck2 += [card2, card1]
        elif card1 > card2:
            deck1 += [card1, card2]
        else:
            deck2 += [card2, card1]

    return(calculate_score(deck1) if len(deck1) > 0 else 0 - calculate_score(deck2))


def part1():
    p1_raw, p2_raw = get_input('./input/input22.txt', '\n\n')
    deck1 = [int(r) for r in p1_raw.split('\n')[1:]]
    deck2 = [int(r) for r in p2_raw.split('\n')[1:]]
    print(play_combat(deck1, deck2))


def part2():
    p1_raw, p2_raw = get_input('./input/input22.txt', '\n\n')
    deck1 = [int(r) for r in p1_raw.split('\n')[1:]]
    deck2 = [int(r) for r in p2_raw.split('\n')[1:]]
    print(play_recursive_combat(deck1, deck2))


if __name__ == "__main__":
    part1()
    part2()
