# 2026 Joel Tann

import sys

def reverse_digits(x):
    rev = 0

    while(x > 0):
        rev += (x % 10)

        x = int(x / 10)

        if (x > 0):
            rev *= 10
    
    return rev

def palindrome(x):
    y = reverse_digits(x)

    if (x == y):
        return True
    else:
        return False
    
for line in sys.stdin:
    line = int(line)

    if (palindrome(line)):
        print(line, "is palindrome")
    else:
        print(line, "is not palindrome")