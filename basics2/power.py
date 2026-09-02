# 2026 Joel Tann

import sys

def power(b, e):
    if (e == 0):
        return 1

    if (e > 0):
        return b * power(b, e-1)


for line in sys.stdin:
    b, e = map(int, line.split())

    print(power(b, e))