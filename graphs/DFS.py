# 2026 Joel Tann

import sys

def DFS(node):
    visited[node] = True

    for neighbour in graph[node]:
        if visited[neighbour] == False:
            DFS(neighbour)

for line in sys.stdin:
    nodes_amount, edges_amount = map(int, line.split())

    if nodes_amount == 0 and edges_amount == 0:
        exit()

    graph = [[] for _ in range(nodes_amount)]
    visited = [False] * nodes_amount

    for i in range(edges_amount):
        a, b = map(int, input().split())

        graph[a].append(b)
        graph[b].append(a)

    DFS(0)

    print(visited)
    print(graph)