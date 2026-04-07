from collections import deque

m, n, h = map(int, input().split())

d = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
graph = []
zero_cnt = 0
for _ in range(h):
    tmp = [list(map(int, input().split())) for _ in range(n)]
    zero_cnt += sum(sub.count(0) for sub in tmp)
    graph.append(tmp)

if zero_cnt == 0:
    print(0)
    exit()

q = deque()
visited = [[[-1 for _ in range(m)] for _ in range(n)] for _ in range(h)]

check = []
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append((i, j, k))
                visited[i][j][k] = 0
            elif graph[i][j][k] == 0:
                check.append((i, j, k))

while q:
    z, x, y = q.popleft()
    
    for i in range(6):
        nz, nx, ny = z + d[i][0], x + d[i][1], y + d[i][2]
        if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and visited[nz][nx][ny] == -1 and graph[nz][nx][ny] == 0:
            q.append((nz, nx, ny))
            visited[nz][nx][ny] = visited[z][x][y] + 1
            
result = -1
for h, x, y in check:
    if visited[h][x][y] == -1:
        result = -1
        break
    
    result = max(result, visited[h][x][y])
    
print(result)