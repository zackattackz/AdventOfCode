from .crate_mover import CrateMover
from .answer import answer_for_cls

def answer(f):
    return answer_for_cls(f, CrateMover)