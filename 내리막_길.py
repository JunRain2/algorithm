import sys
sys.setrecursionlimit(10**5)


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1] * m for _ in range(n)]


def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return 1

    # 이미 계산된 적이 있다면 그대로 반환
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and array[x][y] > array[nx][ny]:
            dp[x][y] += dfs(nx, ny)
    return dp[x][y]


print(dfs(0, 0))
