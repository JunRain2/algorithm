import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

n, m, k = map(int, input().split())  # 도시, 도로, 포장할 도로
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    # 양방향
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra():
    distance = [INF] * (n + 1)
    q = [(0, 1)]
    distance[1] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for b, c in graph[now]:
            cost = c + dist
            if cost < distance[b]:
                distance[b] = cost
                heapq.heappush(q, (cost, b))

# 처음부터 K개의 경로를 0으로 처리?