import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(mid):
    distance = [INF] * (n + 1)
    q = [(0, 1)]
    distance[1] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for nxt, cost in graph[now]:
            new_cost = dist + (cost > mid) # 비용이 더 크면 +1
            if new_cost < distance[nxt]:
                distance[nxt] = new_cost
                heapq.heappush(q, (new_cost, nxt))
    
    return distance[n] <= k

n, p, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(p):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

left, right = 0, 1000000
result = -1

while left <= right:
    mid = (left + right) // 2
    if dijkstra(mid):
        result = mid
        right = mid - 1
    else:
        left = mid + 1

print(result)
