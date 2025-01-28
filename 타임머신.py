import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][k] + graph[k][b], graph[a][b])
            
# 음의 사이클 검사
for i in range(1, n + 1):
    if graph[i][i] < 0:
        print(-1)
        sys.exit()

for i in range(2, n + 1):
    if graph[1][i] < INF:
        print(graph[1][i])
    else:
        print(-1)