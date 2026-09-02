# 2026 Joel Tann

import sys

for line in sys.stdin:
    x = int(line)

    if (x % 2 == 0):
        print("even")
    else:
        print("odd")