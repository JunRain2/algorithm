# 최대 페이지 수 -> 가치
# 남은 기간(무게), 챕터의 수
n, m = map(int, input().split())

dp = [[0] * (n + 1) for _ in range(m + 1)]
for i in range(1, m + 1):
    # 소요되는 일 수, 페이지 수
    w, v = map(int, input().split())
    for j in range(1, n + 1):
        if w > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j - w] + v, dp[i - 1][j])

print(max(dp[m]))
