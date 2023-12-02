def id_str_to_id(id_str):
    return int(id_str[5:])


def set_to_round(set):
    res = {}
    for n, color in set:
        res[color] = int(n)
    return res


def round_str_to_set(round_str):
    return (set_str.strip().split(" ") for set_str in round_str.split(","))


def round_strs_to_rounds(round_strs):
    round_strs = round_strs.split(";")
    round_strs = (round_str.strip() for round_str in round_strs)
    sets = (round_str_to_set(round_str) for round_str in round_strs)
    return (set_to_round(set) for set in sets)


def parse(file):
    for line in file:
        id_str, round_strs = line.split(":")
        yield {"id": id_str_to_id(id_str), "rounds": round_strs_to_rounds(round_strs)}
