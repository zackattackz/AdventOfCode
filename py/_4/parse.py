def parse(f):
    for line in f:
        line = line.rstrip()
        (left, right) = line.split(",")
        n_strs = (left.split("-"), right.split("-"))
        yield [[int(n) for n in side] for side in n_strs]