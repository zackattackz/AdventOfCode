def priority(item):
    isupper = item.isupper()
    lower = item.lower()
    p = ord(lower) - ord('a') + 1
    if isupper:
        p += 26
    return p