import sys
import math
from intervaltree import IntervalTree
from typing import Optional, List
from dataclasses import dataclass


def read_ingredients():
    filename = sys.argv[1]

    with open(filename) as f:
        content = f.read().strip()

    freshStr, availableStr = content.split("\n\n")
    fresh = [(int(f[0]), int(f[1]) + 1)
             for f in map(lambda x: x.split("-"), freshStr.splitlines())]
    available = [int(a) for a in availableStr.splitlines()]
    return fresh, available


if __name__ == "__main__":
    fresh, available = read_ingredients()
    fresh = IntervalTree.from_tuples(fresh)
    fresh.merge_overlaps()
    available_and_fresh_count = sum(1 for a in available if fresh.overlaps(a))
    print("Available and fresh", available_and_fresh_count)
    print("Total fresh", sum(
        [interval.end - interval.begin for interval in fresh]))
