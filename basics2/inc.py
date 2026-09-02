# 2026 Joel Tann

import sys

def inc(x):
    return x + 1

for line in sys.stdin:
    line = int(line)

    print(inc(line))