# 2026 Joel Tann

import sys

def triple(x):
    return x*3

for line in sys.stdin:
    line = int(line)
    print(triple(line))