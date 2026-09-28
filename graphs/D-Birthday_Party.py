# 2026 Joel Tann

import sys

for line in sys.stdin:
    nodes_amount, edges_amount = map(int, line.split())

    if nodes_amount == 0 and edges_amount == 0:
        exit()

    edges = set()
    node_edge_count = list()

    for i in range(edges_amount):
        a, b = map(int, input().split())
        edges.add((a,b))

        if a not in node_edge_count:
            node_edge_count[a] = 0
        if b not in node_edge_count:
            node_edge_count[b] = 0
            
        node_edge_count[a] += 1
        node_edge_count[b] += 1

    for i in node_edge_count:
        if i < 2:
            print("Yes")
            exit()