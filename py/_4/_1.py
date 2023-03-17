from .parse import parse

def is_full_overlap(left_start, left_stop, right_start, right_stop):
    return left_start <= right_start and left_stop >= right_stop

def has_full_overlap(range_pair):
    ((left_start, left_stop), (right_start, right_stop)) = range_pair
    return (
        is_full_overlap(left_start, left_stop, right_start, right_stop) or
        is_full_overlap(right_start, right_stop, left_start, left_stop)
    )

def full_overlap_pair_count(pairs):
    count = 0
    for pair in pairs:
        if has_full_overlap(pair):
            count += 1
    return count

def answer(f):
    return full_overlap_pair_count(parse(f))