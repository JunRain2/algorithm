import heapq

INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

s, t = map(int, input().split())
distance = [INF] * (n + 1)

q = [(0, s)]
distance[s] = 0
while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
        continue
    for b, c in graph[now]:
        cost = c + dist
        if cost < distance[b]:
            distance[b] = cost
            heapq.heappush(q, (cost, b))

print(distance[t])
