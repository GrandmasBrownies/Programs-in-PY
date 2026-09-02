# 2026 Joel Tann

import sys

for line in sys.stdin:
    name, age = line.split()
    age = int(age)
    print(f"{name} is {age} years old.")