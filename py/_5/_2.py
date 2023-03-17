from .crate_mover_9001 import CrateMover9001
from .answer import answer_for_cls

def answer(f):
    return answer_for_cls(f, CrateMover9001)