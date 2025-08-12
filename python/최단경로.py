import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

v, e = map(int, input().split())
start =  int(input())
graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
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

for i in range(1, v + 1):
    if distance[i] < INF:
        print(distance[i])
    else:
        print("INF")