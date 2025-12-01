import sys


def read_instructions(path):
    result = []
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            char = line[0]
            num = int(line[1:])
            result.append((char, num))
    return result


instructions = read_instructions(sys.argv[1])

dial = 50
totalZero = 0

for direction, by in instructions:
    dialBefore = dial
    totalZeroBefore = totalZero

    dial += by if direction == "R" else -by
    if (dialBefore > 0 and dial < 0):
        totalZero += 1
    if (dial == 0):
        totalZero += 1
    totalZero += abs(int(dial / 100))
    dial %= 100

    print(dialBefore, direction, by, dial, totalZero)

print(totalZero)
