# 2026 Joel Tann

import sys

for line in sys.stdin:
    x, y = map(int, line.split())

    if (x < y):
        print("Yes")
    else:
        print("No")