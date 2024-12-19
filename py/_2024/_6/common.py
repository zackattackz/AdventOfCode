def parse(file):
    grid = []
    gpos = None
    for y, l in enumerate(file.readlines()):
        l = l.strip()
        grid.append(l)
        if gpos:
            continue
        for x, c in enumerate(l):
            if c == '^':
                gpos = y, x
    return grid, gpos

def rotate(_dir):
    match _dir:
        case (-1, 0):
            return (0, 1)
        case (0, 1):
            return (1, 0)
        case (1, 0):
            return (0, -1)
        case (0, -1):
            return (-1, 0)
    raise Exception(f"rotate: invalid direction {_dir}")

def movepos(_dir, pos):
    ydir, xdir = _dir
    y, x = pos
    return y + ydir, x + xdir

class OutOfBoundsError(Exception):
    pass

def outofbounds(grid, pos):
    y, x = pos
    return y < 0 or y >= len(grid) or x < 0 or x >= len(grid[y])

def nextpos(grid, _dir, pos, bpos=None):
    newy, newx = movepos(_dir, pos)
    newdir = _dir
    if outofbounds(grid, (newy, newx)):
        raise OutOfBoundsError
    while grid[newy][newx] == '#' or (bpos and (newy, newx) == bpos):
        newdir = rotate(newdir)
        if newdir == _dir:
            raise Exception("guard cannot move: surrounded by walls")
        newy, newx = movepos(newdir, pos)
        if outofbounds(grid, (newy, newx)):
            raise OutOfBoundsError
    return newdir, (newy, newx)

def all_visited(grid, gpos, gdir):
    visited = {gpos}
    while True:
        try:
            gdir, gpos = nextpos(grid, gdir, gpos)
            visited.add(gpos)
        except OutOfBoundsError:
            return visited

