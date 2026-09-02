# 2026 Joel Tann

import sys

def add(x, y):
    return x + y

for line in sys.stdin:
    x, y = map(int, line.split())

    print(add(x, y))