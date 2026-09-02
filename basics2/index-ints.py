# 2026 Joel Tann

import sys

for line in sys.stdin:
    size, *elements, i = map(int, line.split())

    print(elements[i])