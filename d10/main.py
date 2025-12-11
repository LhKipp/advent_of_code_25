from z3 import *
import sys
from functools import reduce
import re
import math
from typing import Optional, List
from dataclasses import dataclass
from scipy.spatial import KDTree
import numpy as np
import networkx as nx
from sympy import symbols, Eq, solve


@dataclass
class Machine:
    indicators: str
    button_rows: list[list[int]]
    joltage_requirements: tuple[int, ...]

    def joltage_all_zero(self) -> tuple[int, ...]:
        return tuple([0] * len(self.joltage_requirements))


def read_machines_from_file(filename):
    with open(filename, "r") as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue

            parts = line.split()
            indicators = parts[0][1:-1]

            buttons = []
            for part in parts[1:-1]:
                buttons.append([int(s) for s in part[1:-1].strip().split(",")])

            # final {...} group
            joltage_requirements = tuple([
                int(s) for s in parts[-1][1:-1].strip().split(",")
            ])

            yield Machine(indicators, buttons, joltage_requirements)


def toggle(indicators: str, buttons: list[int]) -> str:
    indic = bytearray(indicators, "ascii")
    for button in buttons:
        indic[button] ^= ord("#") ^ ord(".")
    return indic.decode()


def increment_joltage(current: tuple[int, ...], buttons: list[int]) -> tuple[int, ...]:
    cur_list = list(current)
    for b in buttons:
        cur_list[b] += 1
    return tuple(cur_list)


def joltage_is_bigger_than_required(required, new_joltage) -> bool:
    for (req, new) in zip(required, new_joltage):
        if new > req:
            return True
    return False


def find_button_press_to_activate(machine: Machine) -> int:
    print("finding buttons to press for", machine)
    # initially all are off
    states: set[tuple[int, ...]] = set([machine.joltage_all_zero()])
    all_seen_states = set([machine.joltage_all_zero()])
    iteration = 0

    while machine.joltage_requirements not in states:
        iteration += 1
        new_states: set[tuple[int, ...]] = set()
        for state in states:
            for buttons in machine.button_rows:
                new_joltage = increment_joltage(state, buttons)
                if joltage_is_bigger_than_required(machine.joltage_requirements, new_joltage):
                    continue
                if new_joltage in all_seen_states:
                    continue
                new_states.add(new_joltage)
                all_seen_states.add(new_joltage)
        states = new_states
        if len(states) == 0:
            print("ERR: no result found")
            exit(1)

    return iteration


def find_lowest_button_presses_until_joltage(joltage_requirements, button_rows):
    n = len(joltage_requirements)
    X = IntVector('x', len(button_rows))

    s = Optimize()
    s.add([x >= 0 for x in X])

    A = []
    for buttons in button_rows:
        row = [0] * n
        for button in buttons:
            row[button] = 1
        A.append(row)

    for i in range(n):
        s.add(Sum(X[k]*A[k][i] for k in range(len(button_rows))) == joltage_requirements[i])
    s.minimize(Sum(X))

    # Check for satisfiability and get the model
    if s.check() == sat:
        model = s.model()
        return sum(model[k].as_long() for k in model)
    else:
        print("No solution found.")


if __name__ == "__main__":
    machines = list(read_machines_from_file(sys.argv[1]))
    # print(machines)
    total = 0
    for machine in machines:
        total += find_lowest_button_presses_until_joltage(machine.joltage_requirements, machine.button_rows)

    print(total)
