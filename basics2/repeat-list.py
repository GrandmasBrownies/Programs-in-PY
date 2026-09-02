# 2026 Joel Tann

import sys

for line in sys.stdin:
    size, *elements = map(int, line.split())

    print(size, "elements:", end='')
    for i in elements:
        print('', i, end='')
    print()