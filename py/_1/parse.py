"""
Parser for Day 1 Part 1 and 2.
"""

from itertools import groupby

def parse(file):
    """
    Parse the given input into a consumable output structure.

    :param file: The input lines.
    :type file: Iterable[str]
    :return: A structure representing all elf inventories.
    :rtype: Iterable[Iterable[int]]
    """

    def split_list(lst, delim):
        """
        Split a list on a given delimeter element into many lists.

        :param lst: The list to split.
        :type lst: List['a]
        :param delim: The delimeter element to split on.
        :type delim: 'a
        :returns: The input list split into many lists.
        :rtype: List[List['a]]
        """

        # Use groupby on unsorted lst to put items != delim into groups.
        # Only take the groups where the key is False.
        return (g for k, g in groupby(lst, lambda x: x == delim) if not k)

    stripped_f = (line.rstrip() for line in file)
    split_stripped_f = split_list(stripped_f, "")
    return ((int(n) for n in ns) for ns in split_stripped_f)
