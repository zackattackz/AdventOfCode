def parse(file):
    return [l.strip() for l in file.readlines()]

def valid_cross(grid, y, x):
    return grid[y][x] == 'A' and ((grid[y-1][x-1] == 'M' and grid[y+1][x+1] == 'S') or (grid[y-1][x-1] == 'S' and grid[y+1][x+1] == 'M')) and ((grid[y-1][x+1] == 'M' and grid[y+1][x-1] == 'S') or (grid[y-1][x+1] == 'S' and grid[y+1][x-1] == 'M'))

def iter_crosses(grid):
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[y]) - 1):
            yield y, x

def count_valid_crosses(grid):
    res = 0
    for y, x in iter_crosses(grid):
        if valid_cross(grid, y, x):
            res += 1
    return res

def answer(file):
    grid = parse(file)
    return count_valid_crosses(grid)

