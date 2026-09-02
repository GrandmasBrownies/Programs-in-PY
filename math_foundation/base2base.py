# 2026 Joel Tann

import sys

for line in sys.stdin:
    number, fbase, tbase = line.split()

    fbase = int(fbase)
    tbase = int(tbase)

    converted = ""

    value = {
        'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17, 'i': 18, 'j': 19, 'k': 20, 'l': 21, 'm': 22, 'n': 23, 'o': 24, 'p': 25,
        'q': 26, 'r': 27, 's': 28, 't': 29, 'u': 30, 'v': 31, 'w': 32, 'x': 33, 'y': 34, 'z': 35
    }

    while (number > 0):
        digit = number % tbase