# 2026 Joel Tann

import sys

for line in sys.stdin:
    word, i, c = line.split()

    i = int(i)

    word = word[:i] + c + word[i+1:]

    print(word)