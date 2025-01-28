n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for x in range(n):
        for y in range(n):
            graph[x][y] = 1 if graph[x][k] + graph[k][y] == 2 else graph[x][y]

for i in range(n):
    print(*graph[i])