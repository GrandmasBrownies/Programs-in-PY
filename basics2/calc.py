# 2026 Joel Tann

import sys

for line in sys.stdin:
    x, o, y = line.split()

    x = float(x)
    y = float(y)

    if (o == '+'):
        print(f"{x + y:.2f}")
    
    if (o == '-'):
        print(f"{x - y:.2f}")

    if (o == '*'):
        print(f"{x * y:.2f}")
    
    if (o == '/'):
        print(f"{x / y:.2f}")
    
    if (o == '^'):
        print(f"{x**y:.2f}")