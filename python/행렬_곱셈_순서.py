n = int(input())
arr = []

for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

INF = int(1e9)

dp = [[INF] * n for _ in range(n)]
for i in range(n):
    dp[i][i] = 0

for step in range(1, n):
    for start in range(n - step):
        end = start + step
        mid = start
        while mid < end:
            sum = arr[start][0] * arr[mid][1] * arr[end][1]
            dp[start][end] = min(dp[start][end], dp[start][mid] + dp[mid + 1][end] + sum)
            mid += 1

print(dp[0][n - 1])