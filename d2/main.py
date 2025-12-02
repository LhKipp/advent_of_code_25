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


def digit_count(n):
    n = abs(n)
    return 1 if n == 0 else int(math.log10(n)) + 1


def find_invalid_ids(start: int, upper_bound: int):
    current = start
    cur_digit_count = digit_count(current)
    if (cur_digit_count % 2) == 1:
        current = int(math.pow(10, cur_digit_count))

    current_str: string = str(current)
    upper_str = current_str[0:len(current_str)//2]
    upper = int(upper_str)
    upper_doubled = int(upper_str + upper_str)

    while upper_doubled < start:
        upper += 1
        upper_str = str(upper)
        upper_doubled = int(upper_str + upper_str)

    while upper_doubled <= upper_bound:
        yield upper_doubled
        upper += 1
        upper_str = str(upper)
        upper_doubled = int(upper_str + upper_str)


if __name__ == "__main__":
    out = read_ranges()
    total = 0
    for start, upper_bound in out:
        total += sum(find_invalid_ids(start, upper_bound))
        for invalid_num in find_invalid_ids(start, upper_bound):
            print(invalid_num)
    print("total is", total)
