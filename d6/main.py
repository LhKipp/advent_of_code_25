import sys
from functools import reduce
import re
import math
from intervaltree import IntervalTree
from typing import Optional, List
from dataclasses import dataclass


def read_problems():
    filename = sys.argv[1]

    with open(filename) as f:
        content = f.read()

    lines = content.splitlines()
    operands = lines[:-1]
    operators = lines[-1]
    print(operands, operators)

    operator_idxs = [m.start() for m in re.finditer(
        r"[+*]", operators)] + [len(operators) + 1]
    for start, end in zip(operator_idxs, operator_idxs[1:]):
        nums = []
        for i in range(start, end - 1):
            nums.append(int("".join([operands[c][i]
                        for c in range(len(operands))])))
        yield nums, operators[start]


if __name__ == "__main__":
    problems = read_problems()

    results = []

    for nums, op in problems:
        print(nums, op)
        op_lambda = (lambda a, b: a + b) if op == '+' else (lambda a, b: a*b)
        results.append(reduce(op_lambda, nums))

    print(sum(results))
