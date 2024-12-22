from .common import all_antinodes, outofbounds, parse

def get_antinodes(grid, y1, x1, y2, x2):
    dy = y2 - y1
    dx = x2 - x1
    ay1, ay2 = y1 - dy, y2 + dy
    ax1, ax2 = x1 - dx, x2 + dx
    for ay, ax in ((ay1, ax1), (ay2, ax2)):
        if not outofbounds(grid, ay, ax):
            yield (ay, ax)

def answer(file):
    grid = parse(file)
    return len(all_antinodes(grid, get_antinodes))

