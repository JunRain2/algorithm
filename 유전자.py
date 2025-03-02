s = input()
n = len(s)
dp = [[0] * n for _ in range(n)]

for i in range(1, n):
    for j in range(n - i):
        if (s[j] == "a" and s[j + i] == "t") or (s[j] == "g" and s[j + i] == "c"):
            dp[j][j + i] = dp[j + 1][j + i - 1] + 2
        for k in range(j, j + i):
            dp[j][j + i] = max(dp[j][j + i], dp[j][k] + dp[k + 1][j + i])
print(dp[0][-1])
