from .priority import priority
from itertools import islice

def parse(f):
    return (l.rstrip() for l in f)

def group_into_triplets(xs):
    for i in range(0, len(xs), 3):
        yield xs[i:i+3]
    

def find_badge(group):
    group_sets = set((frozenset(rucksack) for rucksack in group))
    smallest = min(group_sets)
    group_sets.remove(smallest)

    for item in smallest:
        item_in_groups = (item in group_set for group_set in group_sets)
        if all(item_in_groups):
            return item

def sum_badge_priorities(rucksacks):
    res = 0
    for group in group_into_triplets(rucksacks):
        badge = find_badge(group)
        res += priority(badge)
    return res

def answer(f):
    return sum_badge_priorities(parse(f))