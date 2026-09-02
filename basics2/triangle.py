# 2026 Joel Tann

import sys

for line in sys.stdin:
    x, y, z = map(int, line.split())

    if (x == y and y == z):
        form = "equilateral"

    elif (x + y <= z or x + z <= y or y + z <= x):
        form = ("impossible")

    elif (x != y and x != z and y != z):
        form = "scalene"

    else:
        form = "isosceles"
    
    if ((x*x) + (y*y) == (z*z) or (x*x) + (z*z) == (y*y) or (y*y) + (z*z) == (x*x)):
        angle = "right"
    
    elif((x*x) + (y*y) < (z*z) or (x*x) + (z*z) < (y*y) or (y*y) + (z*z) < (x*x)):
        angle = "obtuse"
    
    else:
        angle = "acute"

    if (form == "impossible"):
        print(form)
    else:
        print(form, angle)

    