from functools import reduce


def first_and_last(vals):
    """
    Returns a tuple of the first and last items of vals, or None if empty.
    If vals has one item, it is both first and last.

    :param vals: What to get first/last from.
    :type vals: Iterable
    :return: tuple of first/last or None if empty
    :rtype:
    """

    if not vals:
        return None
    val = next(vals)
    res = (val, val)
    for val in vals:
        res = (res[0], val)
    return res


def first_and_last_digit(amended_val):
    """
    Returns first_and_last of all digits in amended_val

    :param amended_val: The amended value to find first/last digits in
    :return: first_and_last of the digits
    """

    digits = (c for c in amended_val if c.isdigit())
    return first_and_last(digits)


def answer(file):
    """
    The solution for this part.

    :param file: The problem input.
    :return: The problem solution.
    """
    return sum(
        [int(reduce(lambda a, b: a + b, first_and_last_digit(line))) for line in file]
    )
