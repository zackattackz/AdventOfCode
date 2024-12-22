from .common import all_antinodes, outofbounds, parse

def get_antinodes(grid, y1, x1, y2, x2):
    yield (y1, x1)
    yield (y2, x2)
    dy = y2 - y1
    dx = x2 - x1
    ay = y1 - dy
    ax = x1 - dx
    while not outofbounds(grid, ay, ax):
        yield (ay, ax)
        ay = ay - dy
        ax = ax - dx
    ay = y2 + dy
    ax = x2 + dx
    while not outofbounds(grid, ay, ax):
        yield (ay, ax)
        ay = ay + dy
        ax = ax + dx

def answer(file):
    grid = parse(file)
    return len(all_antinodes(grid, get_antinodes))

