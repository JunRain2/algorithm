s = list(input())
n = len(s)

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n, 0, -1):
    for j in range(i + 1, n + 1):
        if (s[i - 1] == "a" and s[j - 1] == "t") or (s[i - 1] == "g" and s[j - 1] == "c"):
            dp[i][j] = dp[i + 1][j - 1] + 2
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j-1])
        for k in range(i, j + 1):
            dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j])

print(max(map(max, dp)))