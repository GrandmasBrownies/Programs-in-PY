# 2026 Joel Tann

import sys

for line in sys.stdin:
    line = line.strip()
    
    length = len(line) - 1
    total = 0

    for i in line:
        i = int(i)
        total += i * (2 ** length)
        length -= 1
    
    print(total)