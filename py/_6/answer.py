from functools import partial
from .unique import get_n_unique_last_idx

def answer_for_n(f, n):
    return get_n_unique_last_idx(iter(partial(f.read, 1), ''), n) + 1