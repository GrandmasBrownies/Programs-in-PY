# 2026 Joel Tann

import sys

for line in sys.stdin:
    hour = int(line)

    if (4 <= hour <= 11):
        print("Good morning")

    elif (12 <= hour <= 17):
        print("Good afternoon")

    elif (18 <= hour <= 23):
        print("Good evening")

    else:
        print("Hi")