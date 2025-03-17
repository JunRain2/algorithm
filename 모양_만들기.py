from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

        
dx = [-1, 0, 1 ,0]
dy = [0, -1, 0, 1]

def bfs(x, y):
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True
    q = deque([(x, y)])
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
                cnt += 1
                visited[nx][ny] = True
                q.append((nx, ny))
    return cnt

answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            graph[i][j] = 1
            answer = max(answer, bfs(i, j))
            graph[i][j] = 0

print(answer)