from .crate_mover import CrateMover

class CrateMover9001(CrateMover):
    def run_move(self, move):
        to_move = []
        for _ in range(move.qty):
            crate = self.stacks[move.src].pop()
            to_move.append(crate)
        for crate in reversed(to_move):
            self.stacks[move.dst].append(crate)