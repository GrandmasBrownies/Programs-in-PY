# 2026 Joel Tann

import sys

for line in sys.stdin:
    nodes_amount, edges_amount = map(int, line.split())

    if nodes_amount == 0 and edges_amount == 0:
        exit()

    for i in range(edges_amount):
        a, b = map(int, input().split())