import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

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

print(distance[end])
