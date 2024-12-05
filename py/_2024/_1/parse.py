def parse(file):
    for line in file:
        line = line.strip()
        l, r = list(map(int, line.split()))
        yield l, r

