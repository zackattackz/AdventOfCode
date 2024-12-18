DIRECTIONS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

def parse(file):
    return [l.strip() for l in file.readlines()]

def idxs_in_bounds(grid, y, x):
    return 0 <= y < len(grid) and 0 <= x < len(grid[y])

def is_valid_dir(grid, y, x, s, dir_y, dir_x):
    while s:
        y += dir_y
        x += dir_x
        if not idxs_in_bounds(grid, y, x) or grid[y][x] != s[0]:
            return False
        s = s[1:]
    return True

def count_valid_dirs(grid, y, x, s):
    res = 0
    for dir_y, dir_x in DIRECTIONS:
        if is_valid_dir(grid, y, x, s, dir_y, dir_x):
            res += 1
    return res

def count_str(grid, s):
    res = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == s[0] and (n := count_valid_dirs(grid, y, x, s[1:])):
                res += n
    return res

def answer(file):
    grid = parse(file)
    return count_str(grid, 'XMAS')

