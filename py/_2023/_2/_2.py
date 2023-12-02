from .parse import parse
from functools import reduce


def power_cubes(cubes):
    return reduce(lambda a, b: a * b, cubes.values())


def max_cube(rounds, color):
    return max((round.get(color) for round in rounds if round.get(color)))


def max_cubes(game, colors):
    res = {}
    rounds = list(game["rounds"])
    for color in colors:
        max_cube_count = max_cube(rounds, color)
        # Only include colors present in rounds
        if max_cube_count > 0:
            res[color] = max_cube_count
    return res


def answer(file):
    games = parse(file)
    colors = ["red", "green", "blue"]
    return sum((power_cubes(max_cubes(game, colors)) for game in games))
