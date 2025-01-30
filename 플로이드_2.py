INF = int(1e9)

n = int(input())  # 도시
m = int(input())  # 버스의 수

graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

path = [[[] for _ in range(n + 1)] for _ in range(n + 1)] # 2차원 배열의 초기화
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
                path[a][b] = path[a][k] + [k] + path[k][b]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] < INF:
            print(graph[a][b], end=" ")
        else:
            print(0, end=" ")
    print()

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF or graph[a][b] == 0:
            print(0)
        else:
            result = [a, *path[a][b], b]
            print(len(result), *result)
