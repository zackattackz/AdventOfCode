"""
Solution for Day 1 Part 2
"""

from .parse import parse

def get_top_three_sum(elf_inventories):
    """
    Finds the sum of the top three highest-caloric-value elf inventories.

    :param elf_inventories: Given elf inventories to search in.
    :type elf_inventories: Iterable[Iterable[int]]
    :return: The sum of the top three highest-caloric-value elf inventories.
    :rtype: int
    """

    # Sort by caloric-value sum, then sum the top three
    return sum(sorted((sum(inv) for inv in elf_inventories), reverse=True)[:3])

def answer(file):
    """
    The solution for this part.

    :param file: The problem input.
    :type file: Iterable[str]
    :return: The problem solution.
    :rtype: int
    """
    return get_top_three_sum(parse(file))
