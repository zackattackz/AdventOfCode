from .priority import priority

def parse(f):
    for l in f:
        l = l.rstrip()
        yield (l[:len(l)//2], l[len(l)//2:])

def find_duplicate(left, right):
    left_set = set(left)
    for item in right:
        if item in left_set:
            return item

def sum_duplicate_priorities(rucksacks):
    res = 0
    for left, right in rucksacks:
        duplicate = find_duplicate(left, right)
        res += priority(duplicate)
    return res

def answer(f):
    return sum_duplicate_priorities(parse(f))