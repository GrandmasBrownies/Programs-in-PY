# 2026 Joel Tann

import sys

for line in sys.stdin:
    word, i = line.split()
    i = int(i)

    print(word[i])