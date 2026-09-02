# 2026 Joel Tann

import sys

def fibonacci(n):
    f1 = 1
    f2 = 0

    count = 0

    while (count < n):
        temp = f1
        f1 = f1 + f2
        f2 = temp

        count = count + 1
    
    return f2

for line in sys.stdin:
    n = int(line)

    print(fibonacci(n))