# 2026 Joel Tann

import sys

def volume(w, h, d):
    return w * h * d

def area(w, h, d):
    return 2 * ((w * h) + (w * d) + (h * d))

for line in sys.stdin:
    w, h, d = map(int, line.split())

    print(f"The volume of a {w} by {h} by {d} box is {volume(w, h, d)}.")
    print(f"The surface area of a {w} by {h} by {d} box is {area(w, h, d)}.\n")