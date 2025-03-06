from collections import deque

n, m = map(int, input().split())

prev = [list(map(int, input().split())) for _ in range(n)]
result = [list(map(int, input().split())) for _ in range(n)]

if prev == result:
    print("YES")
    exit()

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y, p, r):
    q = deque([(x, y)])
    prev[x][y] = r
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and prev[nx][ny] == p and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
                prev[nx][ny] = r
                

visited = [[False] * m for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and prev[i][j] != result[i][j]:
            bfs(i, j, prev[i][j], result[i][j])
            cnt += 1

if cnt == 1 and prev == result:
    print('YES')
else:
    print('NO')