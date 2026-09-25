n, m = map(int, input().split())

indegree = [0] * (n + 1)
edges = set()

for _ in range(m):
    u, v = map(int, input().split())

    indegree[v] += 1
    edges.add((u, v))

cc = [0] * (n + 1)

for u, v in edges:
    # u follows v
    # If v also follows u, they follow each other
    if (v, u) in edges:
        cc[u] += 1
        cc[v] += 1

for v in range(1, n + 1):
    cc[v] = indegree[v] - cc[v]

best = 1

for v in range(2, n + 1):
    if cc[v] > cc[best]:
        best = v

print(best, cc[best])