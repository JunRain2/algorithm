from collections import deque

# 지을 수 있는 가장 큰 정사각형 목장의 한 변의 크기 L
# 세로, 가로
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]

dx = [1, 1, 0]
dy = [0, 1, 1]


def bfs(x, y):
    q = deque([(x, y)])
    distance = [[-1] * n for _ in range(m)]
    distance[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(3):
            nx, ny = x + dx[i], y + dy[i]
            if (
                0 <= nx < m
                and 0 <= ny < n
                and graph[nx][ny] == 0
            ):
                if distance[nx][ny] == -1:
                    q.append((nx, ny))
                    distance[nx][ny] = distance[x][y] + 1
            else:
                return distance[x][y]


result = 0
visited = [[False] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            result = max(result, bfs(i, j))
print(result)
