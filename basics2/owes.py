# 2026 Joel Tann

import sys

for line in sys.stdin:
    owes, name1, name2 = line.split()
    owes = float(owes)
    
    print(f"{name1} owes ${owes:.2f} dollars to {name2}.")