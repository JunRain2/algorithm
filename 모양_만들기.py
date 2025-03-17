from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1 ,0]
dy = [0, -1, 0, 1]

def bfs(x, y, c):
    visited[x][y] = c
    q = deque([(x, y)])
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1 and graph[nx][ny] == 1:
                cnt += 1
                visited[nx][ny] = c
                q.append((nx, ny))
    return cnt

visited = [[-1] * m for _ in range(n)]
data = []
cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == -1:
            data.append(bfs(i, j, cnt))
            cnt += 1

answer = 0 
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            s = set()
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    s.add(visited[nx][ny])
            tmp = 1
            for k in s:
                if k == -1:
                    continue
                tmp += data[k]
            answer = max(answer, tmp)

print(answer)