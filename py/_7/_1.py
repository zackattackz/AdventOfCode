"""Defines Day 7 Part 1 answer"""

from .parse import parse
from .sum_tree import SumTree

LIMIT = 100000

def answer(problem_input):
    """Get the answer for given problem input"""
    # Parse input into a file tree
    file_tree = parse(problem_input)

    # Create sum tree from the file tree
    sum_tree_iter = iter(SumTree.from_file_tree(file_tree))

    # Return sum of all sum tree directory nodes with value <= LIMIT
    return sum(node.val for node in sum_tree_iter if len(node.children) > 0 and node.val <= LIMIT)
