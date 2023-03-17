from .parse import parse

# elf_inventories: A list of lists of ints
# returns: An int representing the most calories held by one elf


def get_most_calories(elf_inventories):
    return max((sum(elf_inventory) for elf_inventory in elf_inventories))


def answer(f):
    return get_most_calories(parse(f))