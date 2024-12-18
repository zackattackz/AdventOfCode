def parse(file):
    order = {}
    updates = []
    for line in file:
        line = line.strip()
        if line == '':
            break
        pg1 = line[0:2]
        pg2 = line[3:]
        if pg1 in order:
            order[pg1].add(pg2)
        else:
            order[pg1] = {pg2}
    for line in file:
        line = line.strip()
        updates.append(line.split(','))
    return order, updates

