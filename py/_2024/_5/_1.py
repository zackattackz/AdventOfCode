from .common import parse

def update_is_ordered(update, order):
    i = 0
    j = 1
    while j < len(update):
        if not update[j] in order[update[i]]:
            return False
        i += 1
        j += 1
    return True

def answer(file):
    order, updates = parse(file)
    res = 0
    for update in updates:
        if update_is_ordered(update, order):
            res += int(update[len(update) // 2])
    return res

