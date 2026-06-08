# 2026 Joel Tann

def volume(x, y, z):
    return x * y * z

def area(x, y, z):
    return 2*(x*y + x*z + y*z)

w, h, d = map(int, input().split())

print(f"The volume of a {w} by {h} by {d} box is {volume(w, h, d)}.")
print(f"The surface area of a {w} by {h} by {d} box is {area(w, h, d)}.")