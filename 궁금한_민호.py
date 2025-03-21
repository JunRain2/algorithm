n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

data = [[True] * n for _ in range(n)]
for k in range(n):
    for a in range(n):
        for b in range(n):
            if a == b or k == b or k == a:
                continue
            if graph[a][b] == graph[a][k] + graph[k][b]:
                data[a][b] = False
                data[b][a] = False
            elif graph[a][b] > graph[a][k] + graph[k][b]:
                print(-1)
                exit()

answer = 0
for i in range(n):
    for j in range(i + 1, n):
        if data[i][j]:
            answer += graph[i][j]

print(answer)