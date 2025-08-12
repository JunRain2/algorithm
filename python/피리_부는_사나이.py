n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n + 1)]

dir = dict()
dir["D"] = (1, 0)
dir["L"] = (0, -1)
dir["R"] = (0, 1)
dir["U"] = (-1, 0)

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m or visited[x][y] == 2:
        return 0
    if visited[x][y] == 1:
        return 1
    
    visited[x][y] = 1
    nx, ny = x + dir[graph[x][y]][0], y + dir[graph[x][y]][1]
    result = dfs(nx, ny)
    visited[x][y] = 2
    return result

result = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            result += dfs(i, j)
            
print(result)