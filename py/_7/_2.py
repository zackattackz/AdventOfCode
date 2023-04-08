"""Defines Day 7 Part 2 answer."""

from .parse import parse
from .sum_tree import SumTree

MAX_SYS_SPACE = 70000000
MIN_SPACE_NEEDED = 30000000

def answer(problem_input):
    """Get the answer for given problem input"""
    # Parse input into a file tree
    file_tree = parse(problem_input)

    # Create sum tree from the file tree
    root_sum_tree = SumTree.from_file_tree(file_tree)
    sum_tree_iter = iter(root_sum_tree)

    # Only directories (nodes with children).
    sum_tree_directories = (node for node in sum_tree_iter if len(node.children) > 0)

    # Get all node vals that if deleted would satisfy min space needed.
    candidates = (node.val
                  for node in sum_tree_directories
                  if (MAX_SYS_SPACE - (root_sum_tree.val - node.val)) >= MIN_SPACE_NEEDED)

    # Return smallest needed.
    return min(candidates)
