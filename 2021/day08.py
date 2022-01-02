from lib import get_input


def part1():
    data = get_input('./input/input08.txt', '\n')
    code = [[part for part in line.split(" | ")] for line in data]
    unique = sum(len(word) in [2, 3, 4, 7] for line in code for word in line[1].split(" "))
    print(unique)


def get_frequencies(config):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    return {letter: str(config.count(letter)) for letter in list(letters)}


def get_numeric_representation(frequencies, config_word):
    temp = [frequencies[letter] for letter in list(config_word)]
    temp.sort()
    return int(''.join(temp))


def sort_letters(word):
    word = list(word)
    word.sort()
    return ''.join(word)


def part2():
    data = get_input('./input/input08.txt', '\n')
    input = [[part for part in line.split(" | ")] for line in data]

    digits_representation = "abcefg cf acdeg acdfg bcdf abdfg abdefg acf abcdefg abcdfg"
    digit_frequency = get_frequencies(digits_representation)
    digits_value = {}

    for i, digit_representation in enumerate(digits_representation.split(' ')):
        numeric_representation = get_numeric_representation(digit_frequency, digit_representation)
        digits_value[numeric_representation] = str(i)

    summation = 0
    for configuration, numbers in input:
        config_frequencies = get_frequencies(configuration)
        config_digits = {sort_letters(word): digits_value[get_numeric_representation(config_frequencies, word)]
                         for word in configuration.split(' ')}

        summation += int(''.join([config_digits[sort_letters(number)] for number in numbers.split(" ")]))

    print(summation)


if __name__ == "__main__":
    part1()
    part2()
