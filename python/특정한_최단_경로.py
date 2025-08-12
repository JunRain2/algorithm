import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(start, end):
    distance = [INF] * (n + 1)
    q = []
    q.append((0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for b, c in graph[now]:
            cost = dist + c
            if cost < distance[b]:
                distance[b] = cost
                heapq.heappush(q, (cost, b))

    return distance[end]


v1, v2 = map(int, input().split())

result = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
result = min(result, dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n))
if result < INF:
    print(result)
else:
    print(-1)
