from enum import Enum
from typing import Iterable, List

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Grid:
    def __init__(self, grid: List[List[int]]):
        self.grid = grid

    def get_neighbors_above(self, x: int, y: int) -> Iterable[int]:
        for y in reversed(range(y)):
            yield self.grid[y][x]

    def get_neighbors_below(self, x: int, y: int) -> Iterable[int]:
        for y in range(y+1, len(self.grid)):
            yield self.grid[y][x]

    def get_neighbors_left(self, x: int, y: int) -> Iterable[int]:
        return reversed(self.grid[y][:x])

    def get_neighbors_right(self, x: int, y: int) -> Iterable[int]:
        return self.grid[y][x+1:]

    def get_neighbors(self, x: int, y: int, direction: Direction) -> Iterable[int]:
        if direction == Direction.UP:
            return self.get_neighbors_above(x, y)
        elif direction == Direction.DOWN:
            return self.get_neighbors_below(x, y)
        elif direction == Direction.LEFT:
            return self.get_neighbors_left(x, y)
        elif direction == Direction.RIGHT:
            return self.get_neighbors_right(x, y)
        else:
            raise ValueError("Invalid direction.")

    def count_visible_trees(self) -> int:
        directions = (Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT)
        count = 0
        for y, row in enumerate(self.grid):
            for x, tree in enumerate(row):
                all_neighbors = (self.get_neighbors(x, y, d) for d in directions)
                if any(self.is_visible(tree, neighbors) for neighbors in all_neighbors):
                    count += 1
        return count

    @classmethod
    def from_problem_input(cls, problem_input: List[str]):
        grid = []
        for line in problem_input:
            row = []
            for n in line:
                row.append(int(n))
            grid.append(row)
        return cls(grid)

    @staticmethod
    def is_visible(tree: int, neighbors: Iterable[int]) -> bool:
        return all(tree > n for n in neighbors)

