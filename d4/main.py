import sys
import math
from typing import Optional, List
from dataclasses import dataclass


@dataclass
class GridIndex:
    row: int
    col: int

    def adjacent(self) -> list["GridIndex"]:
        dirs = [
            (-1, 0), (1, 0), (0, -1), (0, 1),  # cardinal
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # diagonal
        ]
        return [GridIndex(self.row + dr, self.col + dc) for dr, dc in dirs]


def read_grid():
    filename = sys.argv[1]

    with open(filename) as f:
        content = f.read().strip()

    return [list(line) for line in content.split("\n")]


def index_or_null(grid: list[str], idx: GridIndex) -> Optional[str]:
    if idx.row < 0 or idx.col < 0:
        return None
    if idx.row >= len(grid):
        return None
    row = grid[idx.row]
    if idx.col >= len(grid):
        return None
    return row[idx.col]


def is_accessable(grid: list[str], idx: GridIndex) -> bool:
    adjacent = [index_or_null(grid, adj_idx) for adj_idx in idx.adjacent()]
    adjacent_paper_rolls = sum(1 for x in adjacent if x == "@")
    return adjacent_paper_rolls < 4


if __name__ == "__main__":
    grid = read_grid()

    total = 0
    while True:
        progress = False
        for row_idx in range(len(grid)):
            for col_idx in range(len(grid[row_idx])):
                if grid[row_idx][col_idx] == '@' and is_accessable(grid, GridIndex(row_idx, col_idx)):
                    grid[row_idx][col_idx] = "."
                    total += 1
                    progress = True
        if not progress:
            break
    print(total)
