# 2026 Joel Tann

import sys

for line in sys.stdin:
    x0, y0, x1, y1, x2, y2, x3, y3 = line.split()

    if x0 < x3 and y0 < y3:
        if x2 <= x1 and y2 <= y1:
            print("yes")
        else:
            print("no")
    else:
        if x0 <= x3 and y0 <= y3:
            print("yes")
        else:
            print("no")