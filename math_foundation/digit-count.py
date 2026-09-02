# 2026 Joel Tann

import sys

def digit_count(d, x):
    total = 0
    
    while (x > 0):
        if (d == (x % 10)):
            total += 1
        x = int(x / 10)
        
    return total

for line in sys.stdin:
    d, x = map(int, line.split())

    print(digit_count(d, x))