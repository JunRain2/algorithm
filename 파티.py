import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)

n, m, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start, end):
    distance = [INF] * (n + 1)
    q = []
    q.append((0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for b, c in graph[now]:
            cost = dist + c
            if cost < distance[b]:
                distance[b] = cost
                heapq.heappush(q, (cost, b))
    return distance[end]


result = 0
for i in range(1, n + 1):
    a = dijkstra(i, x)
    b = dijkstra(x, i)
    result = max(result, a + b)

print(result)
