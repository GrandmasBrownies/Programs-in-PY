# 2026 Joel Tann

import sys
import math

def circumference(r):
    return 2 * math.pi * r

def area(r):
    return r * r * math.pi

for line in sys.stdin:
    r = float(line)

    circ = circumference(r)
    ar = area(r)

    print(f"{circ:.2f} {ar:.2f}")