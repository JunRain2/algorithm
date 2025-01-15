import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                heapq.heappush(q, (cost, i[1]))
                distance[i[1]] = cost


for tc in range(int(input())):
    n = int(input())
    graph_value = []
    distance = [INF] * n
    graph = [[] for _ in range(n)]

    for _ in range(n):
        data = list(map(int, input().split()))
        graph_value.append(data)

    dijkstra(0)
    print(graph[n - 1][n - 1])
