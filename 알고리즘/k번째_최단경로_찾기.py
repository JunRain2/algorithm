import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m, k = map(int, input().split())  # 도시, 도로 수, k 번째

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


cnt = [0] * (n + 1)
distance = [[INF] * k for _ in range(n + 1)]
q = [(0, 1)]
distance[1][0] = 0
while q:
    dist, now = heapq.heappop(q)
    # 현재 거리가 k번째 최단 거리보다 크면 무시
    if dist > distance[now][k - 1]:
        continue
    for b, c in graph[now]:
        cost = c + dist
        # k번째 최단 거리보다 작으면 추가
        if distance[b][k - 1] > cost:
            distance[b][k - 1] = cost
            distance[b].sort()  # 정렬하여 k개 유지
            heapq.heappush(q, (cost, b))

for i in range(1, n + 1):
    if max(distance[i]) < INF:
        print(max(distance[i]))
    else:
        print(-1)
