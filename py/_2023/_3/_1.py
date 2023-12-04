from .parse import parse
from itertools import tee


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def overlap(i, length, markers):
    return any(x in markers for x in range(i, length))


def scan_row_part_numbers(row, auxiliary_row):
    res = set()
    for row_x, row_y in pairwise(row):
        if row_x.is_number() and row_y.is_symbol():
            res.add(row_x)
        elif row_y.is_number() and row_x.is_symbol():
            res.add(row_y)
    row_numbers = (elem for elem in row if elem.is_number())
    auxiliary_row_symbols_j = set(
        (elem.j for elem in auxiliary_row if elem.is_symbol())
    )
    for number in row_numbers:
        if overlap(number.j - 1, number.j + len(number) + 1, auxiliary_row_symbols_j):
            res.add(number)

    return res


def part_numbers(schematic):
    res = set()
    for row_a, row_b in pairwise(schematic):
        res |= scan_row_part_numbers(row_a, row_b)
        res |= scan_row_part_numbers(row_b, row_a)
    return res


def answer(file):
    schematic = [list(line) for line in parse(file)]
    return sum(number.item for number in part_numbers(schematic))
