n, m = map(int, input().split())
array = [list(input()) for _ in range(m)]  # B는 파란색 W는 흰색(우리 병사)
result = [0, 0]  # W, B

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

visited = [[False] * n for _ in range(m)]


def dfs(x, y, color):
    visited[x][y] = True
    max_cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and array[nx][ny] == color:
            max_cnt = max(max_cnt, dfs(nx, ny, color))
    return max_cnt + 1


for x in range(m):
    for y in range(n):
        if not visited[x][y]:
            if array[x][y] == "W":
                result[0] += dfs(x, y, "W") ** 2
            else:
                result[1] += dfs(x, y, "B") ** 2

print(*result)
