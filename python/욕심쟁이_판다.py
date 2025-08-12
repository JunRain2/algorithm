import sys
sys.setrecursionlimit(10**5)

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
distance = [[-1] * n for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    result = 0

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[x][y] < graph[nx][ny]:
            if distance[nx][ny] != -1:
                result = max(result, distance[nx][ny])
            else:
                result = max(result, dfs(nx, ny))

    distance[x][y] = result + 1
    return distance[x][y]


result = -1
for i in range(n):
    for j in range(n):
        if distance[i][j] == -1:
            result = max(result, dfs(i, j))


print(result)
