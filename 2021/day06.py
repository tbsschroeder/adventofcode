from lib import get_input


def calc_fishes(start_population, days):
    population = {fish: start_population.count(fish) for fish in range(0, 9)}
    for d in range(0, days):
        new_population = {i: 0 for i in range(0, 9)}
        for day in range(0, 9):
            new_population[day] = population[0 if day + 1 > 8 else day + 1]
        if population[0] > 0:
            new_population[6] += population[0]
        population = new_population
    return sum(population.values())


def part1():
    fishes = list(map(int, get_input('./input/input06.txt', ',')))
    print(calc_fishes(fishes, 80))


def part2():
    fishes = list(map(int, get_input('./input/input06.txt', ',')))
    print(calc_fishes(fishes, 256))


if __name__ == "__main__":
    part1()
    part2()
