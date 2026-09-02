# 2026 Joel Tann

import sys

def digit_sum(x):
    total = 0

    while (x > 0):
        total = total + (x % 10)
        x = int(x / 10)
    
    return total


for line in sys.stdin:
    line = int(line)

    print(digit_sum(line))