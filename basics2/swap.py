# 2026 Joel Tann

import sys

for line in sys.stdin:
    num, string = line.split()
    num = int(num)
    print(string, num)