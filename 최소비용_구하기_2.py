import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)


n = int(input())  # 노드
m = int(input())  # 간선

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

parent = [i for i in range(n + 1)]
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
            parent[b] = now
            distance[b] = cost
            heapq.heappush(q, (cost, b))
            
x = end
result = []
result.append(x)
while x != start:
    x = parent[x]
    result.append(x)
    
    
print(distance[end])
result.reverse()
print(len(result))
print(*result)
