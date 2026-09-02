# 2026 Joel Tann

import sys

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)


for line in sys.stdin:
    x = int(line)
    print(factorial(x))