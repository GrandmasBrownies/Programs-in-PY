# 2026 Joel Tann

import sys

def mult(x, y, z):
    return x * y * z

for line in sys.stdin:
    x, y, z = map(int, line.split())

    print(mult(x, y, z))