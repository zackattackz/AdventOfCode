from .common import parse

def sort_update(update, order):
    presorted = True
    i = 0
    j = 1
    while j < len(update):
        curr_i = i
        curr_j = j
        while curr_i >= 0 and not update[curr_j] in order[update[curr_i]]:
            presorted = False
            temp = update[curr_i]
            update[curr_i] = update[curr_j]
            update[curr_j] = temp
            curr_i -= 1
            curr_j -= 1
        i += 1
        j += 1
    return presorted

def answer(file):
    order, updates = parse(file)
    res = 0
    for update in updates:
        if not sort_update(update, order):
            res += int(update[len(update) // 2])
    return res

