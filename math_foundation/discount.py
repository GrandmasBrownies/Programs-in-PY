# 2026 Joel Tann

import sys

for line in sys.stdin:
    ocupation, age = line.split()

    age = int(age)

    if age < 18:
        print("discount")
    elif ocupation == "student" and age <= 25:
        print("discount")
    elif age >= 65:
        print("discount")
    else:
        print("full price")