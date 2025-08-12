from collections import deque

INF = int(1e9)

n, m = map(int, input().split())
distance = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]


for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


q = deque([(1, 0)])
distance[1] = 0

while q:
    node, dist = q.popleft()
    if dist > distance[node]:
        continue
    for b, c in graph[node]:
        cost = distance[node] + c
        if distance[b] > cost:
            distance[b] = cost
            q.append((b, cost))

print(distance[n])
