def get_n_unique_last_idx(chars, n):
    """
    Finds the last index of the first occurence
    of n unique characters in chars in a row.

    :param chars: An iterable of characters to search in.
    :param n: How many unique characters to search for.
    :returns: The last index if found, -1 if not found.
    """

    def are_unique(xs):
        """
        Check if all items in list xs are unique

        :param xs: A list of hashable items
        :returns: True if all are unique, else False
        """
        return len(set(xs)) == len(xs)

    def rotate(xs, x):
        return [*xs[1:], x]

    last_n = []
    for idx, ch in enumerate(chars):
        # First we need to accumulate n chars
        if len(last_n) < n:
            last_n.append(ch)
            continue
        # Now we can start checking accumulated
        if are_unique(last_n):
            return idx - 1
        last_n = rotate(last_n, ch)

    return -1