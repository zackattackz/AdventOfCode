from .parse import parse
def has_overlap(range_pair):
    ((left_start, left_stop), (right_start, right_stop)) = range_pair
    return left_stop >= right_start and not (left_start > right_stop)

def overlap_pair_count(pairs):
    count = 0
    for pair in pairs:
        if has_overlap(pair):
            count += 1
    return count

def answer(f):
    return overlap_pair_count(parse(f))