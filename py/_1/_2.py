from .parse import parse

def get_top_three_sum(elf_inventories):
    return sum(sorted((sum(inv) for inv in elf_inventories), reverse=True)[:3])

def answer(f):
    return get_top_three_sum(parse(f))