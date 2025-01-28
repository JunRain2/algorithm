import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

q = []
q.append((0, 1))
distance[1] = 0

while q:
    dist, now = heapq.heappop(q)
    if dist < 0:
        print(-1)
        exit()
    if dist > distance[now]:
        continue
    for b, c in graph[now]:
        cost = dist + c
        if cost < distance[b]:
            distance[b] = cost
            heapq.heappush(q, (cost, b))

for i in range(2, n + 1):
    if distance[i] < INF:
        print(distance[i])
    else:
        print(-1)
