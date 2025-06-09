import math


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a, b = find(parent, a), find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())

graph = []
for _ in range(n):
    x, y = map(float, input().split())
    graph.append((x, y))

edges = []

for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = graph[i]
        x2, y2 = graph[j]
        cost = math.hypot(x1 - x2, y1 - y2)
        edges.append((cost, i, j))

parent = list(range(n))

edges.sort()
result = 0
for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

print(f"{result:.2f}")
