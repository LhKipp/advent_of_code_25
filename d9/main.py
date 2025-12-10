import sys
from functools import reduce
import re
import math
from typing import Optional, List
from dataclasses import dataclass
from scipy.spatial import KDTree
import numpy as np
import networkx as nx


def read_points():
    filename = sys.argv[1]

    with open(filename) as f:
        content = f.read()

    points = [line.split(",") for line in content.splitlines()]
    return [(int(x[0]), int(x[1])) for x in points]


def area(p1, p2) -> int:
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)


if __name__ == "__main__":
    points = read_points()
    print(points)

    max_area = 0
    for i in range(len(points)):
        for j in range(len(points)):
            max_area = max(area(points[i], points[j]), max_area)

    print(max_area)
