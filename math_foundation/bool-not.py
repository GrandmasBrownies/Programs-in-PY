import sys

def negation(p):
    return not p

for line in sys.stdin:
    line = line.strip()

    if line == "true":
        neg = negation(True)
    else:
        neg = negation(False)

    neg = str(neg)
    neg = neg.lower()

    print(neg)