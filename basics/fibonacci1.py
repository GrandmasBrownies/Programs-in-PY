# 2026 Joel Tann

#bad fib
def fibonacci(x):
    if (x == 0):
        return 0
    elif (x == 1):
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)

x = int(input())

print(fibonacci(x))