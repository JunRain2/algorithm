from collections import deque
INF = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

hx = [2, 2, -2, -2, 1, 1, -1, -1]
hy = [-1, 1, -1, 1, -2, 2, -2, 2]


k = int(input())
w, h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]

distance = [[[INF] * (k + 1) for _ in range(w)] for _ in range(h)]

q = deque([(0, 0, 0)])
distance[0][0][0] = 0
while q:
    x, y, cnt = q.popleft()
    if cnt < k:
        for i in range(8):
            nx, ny = x + hx[i], y + hy[i]
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] != 1 and distance[nx][ny][cnt + 1] == INF:
                distance[nx][ny][cnt + 1] = distance[x][y][cnt] + 1
                q.append((nx, ny, cnt + 1))
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] != 1 and distance[nx][ny][cnt] == INF:
            distance[nx][ny][cnt] = distance[x][y][cnt] + 1
            q.append((nx, ny, cnt))

result = min(distance[h -1][w - 1])
if result >= INF:
    print(-1)
else:
    print(result)