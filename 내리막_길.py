import sys
sys.setrecursionlimit(10**5)


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return 1
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and array[x][y] > array[nx][ny]:
            cnt += dfs(nx, ny)
    return cnt


print(dfs(0, 0))
