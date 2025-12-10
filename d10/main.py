import sys
from functools import reduce
import re
import math
from typing import Optional, List
from dataclasses import dataclass
from scipy.spatial import KDTree
import numpy as np
import networkx as nx


@dataclass
class Machine:
    indicators: str
    button_rows: list[list[int]]
    joltage_requirements: list[int]


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
            joltage_requirements = [
                int(s) for s in parts[-1][1:-1].strip().split(",")
            ]

            yield Machine(indicators, buttons, joltage_requirements)


def toggle(indicators: str, buttons: list[int]) -> str:
    indic = bytearray(indicators, "ascii")
    for button in buttons:
        indic[button] ^= ord("#") ^ ord(".")
    return indic.decode()


def find_button_press_to_activate(machine: Machine) -> int:
    print("finding buttons to press for", machine)
    # initially all are off
    states: set[str] = set(["." * len(machine.indicators)])
    iteration = 0

    while machine.indicators not in states:
        iteration += 1
        new_states: set[str] = set()
        for state in states:
            for buttons in machine.button_rows:
                new_states.add(toggle(state, buttons))

        states = new_states

    return iteration


if __name__ == "__main__":
    machines = list(read_machines_from_file(sys.argv[1]))
    print(machines)

    total = 0
    for machine in machines:
        total += find_button_press_to_activate(machine)

    print(total)
