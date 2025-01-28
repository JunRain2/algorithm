import sys

input = sys.stdin.readline

INF = int(1e9)

n, m, x = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


result = 0
for i in range(1, n+1):
    result = max(result, graph[i][x] + graph[x][i])

print(result)