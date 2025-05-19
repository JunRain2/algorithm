n, m = map(int, input().split())

graph = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
circle = [[False] * m for _ in range(n)]


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return 1
    
    if visited[x][y]:
        if circle[x][y]:
            return -1
        else:
            return 1

    visited[x][y] = True
    dx = dy = 0
    match graph[x][y]:
        case "D":
            dx += 1
        case "R":
            dy += 1
        case "U":
            dx -= 1
        case "L":
            dy -= 1

    r = dfs(x + dx, y + dy)
    if r == -1:
        circle[x][y] = True

    return r


result = 0
for i in range(n):
    for j in range(m):
        d = dfs(i, j)
        print(d)
        result += d if d != -1 else 0

print(result)
