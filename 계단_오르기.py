n = int(input())
array = [0] * (n + 1)
for i in range(1, n + 1):
    array[i] = int(input())

dp = [0] * (n + 1)
dp[1] = array[1]
if n >= 2:
    dp[2] = dp[1] + array[2]

for i in range(3, n + 1):
    dp[i] = max(dp[i - 2], dp[i - 3] + array[i - 1]) + array[i]


print(dp[n])
