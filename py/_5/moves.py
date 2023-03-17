import re
from collections import namedtuple

Move = namedtuple('Move', ['qty', 'src', 'dst'])

def parse_moves(f):
    line_rgx = r"move (\d+) from (\d+) to (\d+)$"
    for line in f:
        search = re.search(line_rgx, line)
        qty = int(search.group(1))
        src = int(search.group(2)) - 1
        dst = int(search.group(3)) - 1
        yield Move(qty,src,dst)