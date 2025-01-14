n = int(input())

array = []
for _ in range(n):
    t, p = map(int, input().split())
    array.append((t, p))

dp = [0] * (n + 1)

for i in range(n):
    t, p = array[i]
    day = i + t
    if day <= n:
        for j in range(day, n + 1):
            dp[j] = max(dp[j], p + dp[i])

print(max(dp))
