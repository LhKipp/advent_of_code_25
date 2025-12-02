import sys
import math


def read_ranges():
    filename = sys.argv[1]

    with open(filename) as f:
        line = f.read().strip()

    ranges = []
    for part in line.split(","):
        start, end = part.split("-")
        ranges.append((int(start), int(end)))

    return ranges


if __name__ == "__main__":
    out = read_ranges()
    total = 0
    for start, upper_bound in out:
        for i in range(start, upper_bound + 1):
            i_str = str(i)
            for take_chars in range(1, len(i_str) // 2 + 1):
                check = i_str[0:take_chars] * (len(i_str) // take_chars)
                # print("Checking", i_str, "take_chars", take_chars, "check str", check)
                if check == i_str:
                    print("invalid id found:", i_str)
                    total += i
                    break
    print(total)
