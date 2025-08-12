from collections import deque

INF = int(1e9)

n, m, k = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
distance = [[[INF] * (k + 1) for _ in range(m)] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

q = deque([(0, 0, 0)])
distance[0][0][0] = 1
while q:
    x, y, c = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if c < k and graph[nx][ny] == 1 and distance[nx][ny][c + 1] == INF:
                distance[nx][ny][c + 1] = distance[x][y][c] + 1
                q.append((nx, ny, c + 1))
            elif distance[nx][ny][c] == INF and graph[nx][ny] == 0:
                distance[nx][ny][c] = distance[x][y][c] + 1
                q.append((nx, ny, c))

result = min(distance[n - 1][m - 1])
if result >= INF:
    print(-1)
else:
    print(result)
