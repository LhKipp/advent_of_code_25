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
    return [[int(x[0]), int(x[1]), int(x[2])] for x in points]


if __name__ == "__main__":
    points = read_points()

    tree = KDTree(points)

    min_pairs = list(tree.query_pairs(100000))
    if len(min_pairs) < 1000:
        raise Exception("len")
    min_pairs = [(x[0], x[1], math.dist(
        points[x[0]], points[x[1]])) for x in min_pairs]
    min_pairs.sort(key=lambda x: x[2])
    min_pairs = min_pairs[:1000]
    print(min_pairs)

    G = nx.Graph()
    G.add_edges_from([(x[0], x[1]) for x in min_pairs])

    components = list(nx.connected_components(G))
    print(components)
    print((sorted([len(c) for c in components], reverse=True)[:3]))
