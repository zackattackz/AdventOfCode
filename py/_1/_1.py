"""
Solution for Day 1 Part 1
"""

from .parse import parse

def get_most_calories(elf_inventories):
    """
    Finds the highest-caloric-value elf inventory.

    :param elf_inventories: Given elf inventories to search in.
    :type elf_inventories: Iterable[Iterable[int]]
    :return: The highest-caloric-value elf inventory.
    :rtype: int
    """
    return max(sum(elf_inventory) for elf_inventory in elf_inventories)

def answer(file):
    """
    The solution for this part.

    :param file: The problem input.
    :type file: Iterable[str]
    :return: The problem solution.
    :rtype: int
    """
    return get_most_calories(parse(file))
