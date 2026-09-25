# 2026 Joel Tann

import sys

def conjunction(p, q):
    if p == True and q == True:
        return True
    else:
        return False

def disjunction(p, q):
    if p == True or q == True:
        return True
    else:
        return False

for line in sys.stdin:
    p, b, q = line.split()

    if p == "true":
        p = True
    else:
        p = False

    if q == "true":
        q = True
    else:
        q = False

    if b == "and":
        result = conjunction(p, q)
    elif b == "or":
        result = disjunction(p, q)


    result = str(result)
    result = result.lower()

    print(result)