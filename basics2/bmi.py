# 2026 Joel Tann

import sys

for line in sys.stdin:
    h, w = map(float, line.split())
    bmi = float(w / (h**2))

    if (bmi < 18.5):
        print("underweight")
    elif (bmi < 25):
        print("normal weight")
    elif (bmi < 30):
        print("overweight")
    else:
        print("obese")
