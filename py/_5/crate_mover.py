def split_by_four(xs):
    args = [iter(xs)] * 4
    return zip(*args)

class CrateMover:
    def __init__(self, stacks):
        self.stacks = stacks

    @classmethod
    def from_file(cls, f):
        crate_rows = CrateMover.parse_crates(f)
        return cls(CrateMover.stacks_from_crate_rows(crate_rows))

    def run_move(self, move):
        for _ in range(move.qty):
            crate = self.stacks[move.src].pop()
            self.stacks[move.dst].append(crate)

    def run_moves(self, moves):
        for move in moves:
            self.run_move(move)

    def get_top_crates(self):
        for stack in self.stacks:
            yield stack[len(stack)-1]

    @staticmethod
    def parse_crates(f):
        def parse_crate(crate_str):
            return crate_str[1]
        
        eof = '1'
        current = []
        for line in f:
            crate_strs = split_by_four(line)

            # Check first crate_str to see if it's eof
            crate_str = next(crate_strs)
            crate = parse_crate(crate_str)
            if crate == eof:
                break

            # Append to current if it's not eof
            current.append(crate)

            # Parse remaining crates
            for crate_str in crate_strs:
                current.append(parse_crate(crate_str))

            yield current
            current = []

    @staticmethod
    def stacks_from_crate_rows(crate_rows):
        def rstrip(stack):
            for crate in stack:
                if crate  == ' ':
                    break
                yield crate
        return [list(rstrip((reversed(stack)))) for stack in zip(*crate_rows)]

