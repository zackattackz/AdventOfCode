def parse(file):
    for line in file:
        yield map(int, line.strip().split())

def safe_distance(lv1, lv2):
    diff = abs(lv1 - lv2)
    return 1 <= diff <= 3

def safe_levels(lv1, lv2, inc):
    if inc and lv1 > lv2:
        return False
    if not inc and lv1 < lv2:
        return False
    if not safe_distance(lv1, lv2):
        return False
    return True

def report_safe(report):
    if len(report) < 2:
        return True
    if len(report) == 2:
        return safe_distance(report[0], report[1])
    inc = report[0] < report[1]
    i, j = 0, 1
    while j < len(report):
        if not safe_levels(report[i], report[j], inc):
            return False
        i += 1
        j += 1
    return True

