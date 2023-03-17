from itertools import groupby

# path: path to file containing elf_inventories structure
# returns: A list of lists of ints that is the parsed file
def parse(f):
    def split_list(l, delim):
        return (g for k, g in groupby(l, lambda x: x == delim) if not k)
    
    stripped_f = (line.rstrip() for line in f)
    split_stripped_f = split_list(stripped_f, "")
    return ((int(n) for n in ns) for ns in split_stripped_f)