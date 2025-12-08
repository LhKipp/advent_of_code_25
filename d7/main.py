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
    beam_counts = [0 for i in range(len(grid[0]))]

    beams.add(grid[0].find('S'))
    beam_counts[grid[0].find('S')] += 1

    splitted_total = 0
    for row_idx in range(1, len(grid)):
        new_beams = set()
        new_beam_counts = [0 for i in range(len(grid[0]))]

        for beam in beams:
            next_spot = grid[row_idx][beam]
            if next_spot == '.':
                new_beams.add(beam)
                new_beam_counts[beam] += beam_counts[beam]
            elif next_spot == '^':
                splitted_total += 1
                if beam > 0:
                    new_beams.add(beam - 1)
                    new_beam_counts[beam - 1] += beam_counts[beam]
                if beam < len(grid[0]):
                    new_beams.add(beam + 1)
                    new_beam_counts[beam + 1] += beam_counts[beam]
        beams = new_beams
        beam_counts = new_beam_counts
        print("row_idx %2d, beam_counts %2d" % (row_idx, sum(beam_counts)), "beams", beam_counts)
    print(sum(beam_counts))


if __name__ == "__main__":
    grid = read_grid()
    progress_beams(grid)
