import sys
import math
from intervaltree import IntervalTree
from typing import Optional, List
from dataclasses import dataclass


def read_problems():
    filename = sys.argv[1]

    with open(filename) as f:
        content = f.read().strip()

    lines = [[v.strip() for v in line.split()]
             for line in content.splitlines()]
    return [[int(v) for v in line] for line in lines[:-1]] + [lines[-1]]


if __name__ == "__main__":
    problems = read_problems()
    print(problems)

    count_operands = len(problems) - 1
    operator_idx = count_operands
    count_problems = len(problems[0])

    results = []

    for problem_idx in range(count_problems):
        def op(a, b):
            opc = problems[count_operands][problem_idx]
            result = a + b if opc == '+' else a * b
            print(a, opc, b, "=", result)
            return result

        total = problems[0][problem_idx]
        for i in range(1, count_operands):
            total = op(total, problems[i][problem_idx])
        results.append(total)

    print(sum(results))
