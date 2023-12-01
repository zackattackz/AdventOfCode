from .grid import Grid
from typing import List

def answer(problem_input: List[str]) -> int:
    problem_input = (line.rstrip() for line in problem_input)
    return Grid.from_problem_input(problem_input).count_visible_trees()
