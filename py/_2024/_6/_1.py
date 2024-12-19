from .common import all_visited, parse

def answer(file):
    grid, gpos = parse(file)
    gdir = -1, 0
    visited = all_visited(grid, gpos, gdir)
    return len(visited)

