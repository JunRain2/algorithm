n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

d = dict({"D": (1, 0), "U": (-1, 0), "L": (0, -1), "R": (0, 1)})


def dfs(x, y, visited):
    if x < 0 or x >= n or y < 0 or y >= m or visited[x][y]:
        return 0

    visited[x][y] = True
    dx, dy = x + d[graph[x][y]][0], y + d[graph[x][y]][1]
    return dfs(dx, dy, visited) + 1


result = 0
for i in range(n):
    for j in range(m):
        visited = [[False] * m for _ in range(n)]
        result = max(dfs(i, j, visited), result)

print((n * m) - result)
