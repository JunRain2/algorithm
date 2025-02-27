dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

hx = [2, 2, -2, -2, 1, 1, -1, -1]
hy = [-1, 1, -1, 1, -2, 2, -2, 2]


k = int(input())
w, h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]

dp = dict()


def dfs(x, y, visited, cnt):
    if x < 0 or x >= h or y < 0 or y >= w or graph[x][y] == 1 or visited[x][y]:
        return int(1e9)
    if x == (h - 1) and y == (w - 1):
        return 0
    if (x, y, cnt) in dp:
        return dp[(x, y, cnt)]

    visited[x][y] = True

    result = int(1e9)
    if cnt < k:
        for i in range(8):
            nx, ny = x + hx[i], y + hy[i]
            result = min(result, dfs(nx, ny, visited, cnt + 1))

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        result = min(result, dfs(nx, ny, visited, cnt))

    visited[x][y] = False

    dp[(x, y, cnt)] = result + 1
    return dp[(x, y, cnt)]


visited = [[False] * w for _ in range(h)]
result = dfs(0, 0, visited, 0)
if result >= int(1e9):
    print(-1)
else:
    print(result)
