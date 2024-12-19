from .common import OutOfBoundsError, all_visited, parse, nextpos

def blocking_will_loop(grid, gdir, gpos, bpos):
    fast_gpos, fast_gdir = gpos, gdir
    while True:
        try:
            gdir, gpos = nextpos(grid, gdir, gpos, bpos)
            fast_gdir, fast_gpos = nextpos(grid, fast_gdir, fast_gpos, bpos)
            fast_gdir, fast_gpos = nextpos(grid, fast_gdir, fast_gpos, bpos)
            if gpos == fast_gpos and gdir == fast_gdir:
                return True
        except OutOfBoundsError:
            return False

def answer(file):
    grid, gpos = parse(file)
    gdir = -1, 0
    visited = all_visited(grid, gpos, gdir)
    blockers = 0
    for bpos in visited - {gpos}:
        if blocking_will_loop(grid, gdir, gpos, bpos):
            blockers += 1
    return blockers

