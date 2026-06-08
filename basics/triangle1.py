# 2026 Joel Tann

x, y, z = map(int, input().split())

if (x == y and y == z):
    print("equilateral")

elif (x + y <= z or x + z <= y or y + z <= x):
    print("impossible")

elif (x != y and x != z and y != z):
    print("scalene")

else:
    print("isosceles")