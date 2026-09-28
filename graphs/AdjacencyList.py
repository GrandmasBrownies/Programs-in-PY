# 2026 Joel Tann

import sys

for line in sys.stdin:
    nodes_amount, edges_amount = map(int, line.split())

    if nodes_amount == 0 and edges_amount == 0:
        exit()

    graph = [[] for _ in range(nodes_amount)] # Empty list for all indexes up to nodes_amount

    for i in range(edges_amount):
        a, b = map(int, input().split())

        graph[a].append(b)
        graph[b].append(a)

    print(graph)