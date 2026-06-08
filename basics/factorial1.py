# 2026 Joel Tann

def factorial(x):
    total = x

    while (x > 2):
        total *= (x-1)
        x -= 1

    if (total > 1):
        return total
    else:
        return 1

x = int(input())

print(factorial(x))