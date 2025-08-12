import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(x, y):
    array[x][y] = 0
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and array[nx][ny] == 1:
            cnt += dfs(nx, ny)
    return cnt + 1
    
result = 0
max_width = 0
for i in range(n):
    for j in range(m):
        if array[i][j] == 1:
            result += 1
            max_width = max(max_width, dfs(i,j))

print(result)
print(max_width)
