# 물건의 수, 버틸 수 있는 무게
n, k = map(int, input().split())
# 행 -> 물건의 수, 열 -> 무게
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    w, v = map(int, input().split())
    for j in range(1, k + 1):
        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j - w] + v, dp[i - 1][j])

print(max(dp[n]))
