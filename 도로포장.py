import heapq
import sys

input = sys.stdin.readline
INF = int(1e18)  # 더 큰 값으로 INF 설정 -> "걸리는 시간 * 도로의 수"가 int(1e9)를 초과

n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

distance = [[INF] * (k + 1) for _ in range(n + 1)]
q = [(0, 1, 0)]  # (비용, 현재 도시, 포장한 도로 수)
distance[1][0] = 0

while q:
    dist, now, paved = heapq.heappop(q)

    if dist > distance[now][paved]:
        continue

    for b, c in graph[now]:
        # 도로를 포장하지 않는 경우
        cost = dist + c
        if cost < distance[b][paved]:
            distance[b][paved] = cost
            heapq.heappush(q, (cost, b, paved))

        # 도로를 포장하는 경우
        if paved < k and dist < distance[b][paved + 1]:
            distance[b][paved + 1] = dist
            heapq.heappush(q, (dist, b, paved + 1))

print(min(distance[n]))
