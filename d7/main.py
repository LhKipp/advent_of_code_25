import sys
from functools import reduce
import re
import math
from intervaltree import IntervalTree
from typing import Optional, List
from dataclasses import dataclass


def read_grid():
    filename = sys.argv[1]

    with open(filename) as f:
        content = f.read()

    return content.splitlines()


def progress_beams(grid: list[str]):
    beams = set()
    beams.add(grid[0].find('S'))

    splitted_total = 0
    for row_idx in range(1, len(grid)):
        new_beams = set()
        for beam in beams:
            next_spot = grid[row_idx][beam]
            if next_spot == '.':
                new_beams.add(beam)
            elif next_spot == '^':
                splitted_total += 1
                if beam > 0:
                    new_beams.add(beam - 1)
                if beam < len(grid[0]):
                    new_beams.add(beam + 1)
        print("row_idx", row_idx, "splitted_total", splitted_total)
        beams = new_beams
    print(splitted_total)


if __name__ == "__main__":
    grid = read_grid()
    progress_beams(grid)
