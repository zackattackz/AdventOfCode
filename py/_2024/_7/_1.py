from operator import add, mul
from .common import parse, sum_valid_test_vals

def answer(file):
    equations = parse(file)
    return sum_valid_test_vals(equations, [add, mul])

