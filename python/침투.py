import sys
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y, visited):
    if x < 0 or x >= n or y < 0 or y >= m or visited[x][y] or graph[x][y] == 1:
        return
    if x == (n - 1):
        return True
    
    visited[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if dfs(nx, ny, visited):
            return True

    
visited = [[False] * m for _ in range(n)]
for i in range(m):
    if not visited[0][i]:
        if dfs(0, i, visited):
            print("YES")
            exit()

print('NO')