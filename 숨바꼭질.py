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


distance = [0 if x == INF else x for x in distance] # 리스트에서 특정 값만 변경
max_distance = max(distance)
indeces = [i for i, x in enumerate(distance) if x == max_distance] # 리스트에서 특정 값을 갖는 인덱스를 반환

print(indeces[0], max_distance, len(indeces))
