import sys
import math


def read_bank():
    filename = sys.argv[1]

    with open(filename) as f:
        line = f.read().strip()

    return line.split("\n")


def largest_possible_joltage(bank: str):
    result = ""
    read_ahead = 0
    print("bank is", bank)
    for i in range(11, -1, -1):
        bank_rest = bank[read_ahead:-i] if i != 0 else bank[read_ahead:]
        print(bank_rest, read_ahead, i)
        max_battery_idx, max_battery = max(
            enumerate(bank_rest), key=lambda x: x[1])
        result += max_battery
        read_ahead += max_battery_idx + 1
    print("bank is", bank, "result is", result)
    return int(result)


if __name__ == "__main__":
    banks = read_bank()

    print(sum(largest_possible_joltage(bank)for bank in banks))
