# 2026 Joel Tann

import sys

for line in sys.stdin:
    nodes_amount, edges_amount = map(int, line.split())

    if nodes_amount == 0 and edges_amount == 0:
        exit()

    edges = set()
    node_edge_count = [0] * nodes_amount

    for i in range(edges_amount):
        a, b = map(int, input().split())
        edges.add((a,b))
            
        node_edge_count[a] += 1
        node_edge_count[b] += 1

    for i in node_edge_count:
        if i < 2:
            print("Yes")
            break
    else:
        print("No")
