from .moves import parse_moves

def parse(f, crate_mover_cls):
    crate_mover = crate_mover_cls.from_file(f)
    # Skip the blank seperator line
    next(f)
    return crate_mover, parse_moves(f)

def answer_for_cls(f, crate_mover_cls):
    crate_mover, moves = parse(f, crate_mover_cls)
    crate_mover.run_moves(moves)
    return ''.join(crate_mover.get_top_crates())