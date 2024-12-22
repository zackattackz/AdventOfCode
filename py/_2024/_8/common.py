def is_antenna(c):
    return c.isalnum()

def parse(file):
    grid = {
        "ylen": 0,
        "xlen": 0,
        "coords": {}
    }
    coords = grid["coords"]
    for y, line in enumerate(file):
        line = line.strip()
        grid["ylen"] += 1
        grid["xlen"] = len(line)
        for x, c in enumerate(line):
            if not is_antenna(c):
                continue
            if c in coords and y in coords[c]:
                coords[c][y].add(x)
            elif c in coords:
                coords[c][y] = {x}
            else:
                coords[c] = {y: {x}}
    return grid

def outofbounds(grid, y, x):
    return y < 0 or y >= grid["ylen"] or x < 0 or x >= grid["xlen"]

def antenna_pairs(coords):
    for c in coords:
        for y1 in coords[c]:
            for x1 in coords[c][y1]:
                for y2 in coords[c]:
                    for x2 in coords[c][y2]:
                        if y1 != y2 or x1 != x2:
                            yield (y1, x1), (y2, x2)

def all_antinodes(grid, get_antinodes):
    res = set()
    for (y1, x1), (y2, x2) in antenna_pairs(grid["coords"]):
        for ay, ax in get_antinodes(grid, y1, x1, y2, x2):
            res.add((ay, ax))
    return res

