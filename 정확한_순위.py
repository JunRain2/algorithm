import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

visited = [[False] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            continue
        else:
            visited[i][j] = True
            visited[j][i] = True

result = []
for i in range(1, n + 1):
    flag = True
    for j in range(1, n + 1):
        if not visited[i][j]:
            flag = False
    if flag:
        result.append(i)

print(len(result))
