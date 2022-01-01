from lib import get_input
import sys


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


def get_crab_fuel(start, end):
    fuel = 0
    step = 1
    for _ in range(start, end, 1 if start < end else -1):
        fuel += step
        step = step + 1
    return fuel


def part1():
    crabs = list(map(int, get_input('./input/input07.txt', ',')))
    fuel = sys.maxsize
    for line in range(min(crabs), max(crabs) + 1):
        tmp = sum([abs(line - crab) for crab in crabs])
        if tmp < fuel:
            fuel = tmp
    print(fuel)


def part2():
    crabs = list(map(int, get_input('./input/input07.txt', ',')))
    fuel = sys.maxsize
    for line in range(min(crabs), max(crabs) + 1):
        tmp = sum([get_crab_fuel(line, crab) for crab in crabs])
        if tmp < fuel:
            fuel = tmp
    print(fuel)


if __name__ == "__main__":
    part1()
    part2()
