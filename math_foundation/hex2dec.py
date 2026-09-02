# 2026 Joel Tann

import sys

""" for line in sys.stdin:
    line = line.strip()

    length = len(line) - 1
    total = 0

    for i in line:
        if (i == 'a'):
            total += 10 * (16**length)
            length -= 1
        elif (i == 'b'):
            total += 11 * (16**length)
            length -= 1
        elif (i == 'c'):
            total += 12 * (16**length)
            length -= 1
        elif (i == 'd'):
            total += 13 * (16**length)
            length -= 1
        elif (i == 'e'):
            total += 14 * (16**length)
            length -= 1
        elif (i == 'f'):
            total += 15 * (16**length)
            length -= 1
        else:
            total += int(i) * (16**length)
            length -= 1
    print(total) """

for line in sys.stdin:
    line = line.strip()

    print(int(line, 16))