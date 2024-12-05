from collections import Counter
from .parse import parse

def answer(file):
    left_ids = set()
    right_counter = Counter()
    for l, r in parse(file):
        left_ids.add(l)
        right_counter.update([r])
    return sum(l * right_counter[l] for l in left_ids)

