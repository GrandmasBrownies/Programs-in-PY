# 2026 Joel Tann

import sys

for line in sys.stdin:
    t0, t1, t2, t3 = line.split()

    h0, m0 = map(int, t0.split(':'))
    h1, m1 = map(int, t1.split(':'))
    h2, m2 = map(int, t2.split(':')) 
    h3, m3 = map(int, t3.split(':'))

    if h0 < h3:
        if h1 > h2 or (h1 == h2 and m1 > m2):
            print("conflict")
        else:
            print("ok")
    else:
        if h2 > h1 or (h2 == h1 and m2 > m1):
            print("conflict")
        else:
            print("ok")