from .parse import parse


def round_possible(round, limits):
    return all((n <= limits[color] for color, n in round.items()))


def game_possible(game, limits):
    return all((round_possible(round, limits) for round in game["rounds"]))


def possible_games(games, limits):
    return (game for game in games if game_possible(game, limits))


def answer(file):
    limits = {"red": 12, "green": 13, "blue": 14}

    games = parse(file)

    return sum((game["id"] for game in possible_games(games, limits)))
