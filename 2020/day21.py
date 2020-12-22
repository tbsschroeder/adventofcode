from lib import get_input
import re


def read_food(data):
    foods = []
    for line in data:
        ingredients, allergens = line.split(" (contains ")
        ingredients = set([i for i in ingredients.split(" ")])
        allergens = set([a for a in allergens[:-1].split(", ")])
        foods.append((ingredients, allergens))
    return foods


def part1():
    data = get_input('./input/input21.txt', '\n')
    foods = read_food(data)

    foodCount = {}
    possible = {}
    for ingredients, allergens in foods:
        for ingredient in ingredients:
            if ingredient in foodCount.keys():
                foodCount[ingredient] += 1
            else:
                foodCount[ingredient] = 1

        for allergen in allergens:
            if allergen in possible:
                possible[allergen] &= ingredients
            else:
                possible[allergen] = ingredients.copy()

    allergic = {item for ingAllergens in possible.values()
                for item in ingAllergens}
    print(sum(foodCount[ing] for ing in (foodCount.keys() - allergic)))


def part2():
    data = get_input('./input/input21.txt', '\n')
    foods = read_food(data)

    possible = {}
    for ingredients, allergens in foods:
        for allergen in allergens:
            if allergen in possible:
                possible[allergen] &= ingredients
            else:
                possible[allergen] = ingredients.copy()

    found = set()
    allergenMap = []
    while len(allergenMap) < len(possible.keys()):
        for allergen, ingredients in possible.items():
            if len(ingredients - found) == 1:
                ing = min(ingredients - found)
                allergenMap.append((allergen, ing))
                found.add(ing)
                break

    print(",".join(x[1] for x in sorted(allergenMap)))


if __name__ == "__main__":
    part1()
    part2()
