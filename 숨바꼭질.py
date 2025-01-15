import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

q = []
distance[1] = 0
heapq.heappush(q, (0, 1))
while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

# 최단 거리가 가장 먼 노드 번호
max_node = 0
# 도달할 수 있는 노드 중에서, 최단 거리가 가장 먼 노드와의 최단 거리
max_distance = 0
# 최단 거리가 가장 먼 노드와의 최단 거리와 동일한 최단 거리를 가지는 노드들의 리스트
result = []

for i in range(1, n + 1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif max_distance == distance[i]:
        result.append(i)
        
print(max_node, max_distance, len(result))