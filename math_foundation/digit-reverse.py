# 2026 Joel Tann

import sys

def reverse_digits(x):
    rev = 0

    while(x > 0):
        rev += (x % 10)

        x = int(x / 10)

        if (x > 0):
            rev *= 10
    
    return rev

for line in sys.stdin:
    line = int(line)

    print(reverse_digits(line))