import copy

r, c, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]

up = 0

for i in range(r):
    if graph[i][0] == -1:
        up = i
        break

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def spread(x, y, data):
    v = graph[x][y] // 5
    cnt = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
            cnt += 1
            data[nx][ny] += v

    data[x][y] += graph[x][y] - (cnt * v)


for i in range(t):
    data = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j] == -1:
                data[i][j] = -1
            elif graph[i][j] > 0:
                spread(i, j, data)

    graph = copy.deepcopy(data)

    for i in range(r):
        for j in range(c):
            if graph[i][j] == -1:
                continue
            if i <= up:
                # 1순위
                if i == up:
                    if j == 1:
                        data[i][j] = 0
                    else:
                        data[i][j] = graph[i][j - 1]
                # 2순위
                elif j == (c - 1):
                    data[i][j] = graph[i + 1][j]
                # 3순위
                elif i == 0:
                    data[i][j] = graph[i][j + 1]
                # 4순위
                elif j == 0:
                    data[i][j] = graph[i - 1][j]
            else:
                if i == (up + 1):
                    if j == 1:
                        data[i][j] = 0
                    else:
                        data[i][j] = graph[i][j - 1]
                elif j == (c - 1):
                    data[i][j] = graph[i - 1][j]
                elif i == (r - 1):
                    data[i][j] = graph[i][j + 1]
                elif j == 0:
                    data[i][j] = graph[i + 1][j]
    graph = data

print(sum(map(sum, graph)) + 2)
