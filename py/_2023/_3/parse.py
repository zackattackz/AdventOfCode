from dataclasses import dataclass


@dataclass
class Element:
    i: int
    j: int
    item: int | str
    len: int

    def is_number(self):
        return isinstance(self.item, int)

    def is_symbol(self):
        return not self.is_number() and self.item != "."

    def __len__(self):
        return self.len

    def __hash__(self):
        return hash((self.i, self.j, self.item, self.len))


def parse_line(line, i):
    current_num_str = ""
    current_num_j = None
    for j, c in enumerate(line):
        if c.isdigit() and current_num_j:
            current_num_str += c
        elif c.isdigit():
            if current_num_j is None:
                current_num_j = j
            current_num_str += c
        elif current_num_j is not None:
            yield Element(i, current_num_j, int(current_num_str), len(current_num_str))
            current_num_j = None
            current_num_str = ""
            yield Element(i, j, c, 1)
        else:
            yield Element(i, j, c, 1)
    if current_num_j:
        yield Element(i, current_num_j, int(current_num_str), len(current_num_str))


def parse(file):
    return (parse_line(line.strip(), i) for i, line in enumerate(file))
