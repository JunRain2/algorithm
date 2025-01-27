n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

dp = [0] * (n + 1)
dp[1] = array[0]

cnt = -1
for i in range(2, n + 1):
    a, b = dp[i - 1], dp[i - 2]
    if a <= b or cnt == 1:
        cnt = 0
        dp[i] = b + array[i - 1]
    else:
        cnt += 1
        dp[i] = a + array[i - 1]


print(dp[n])
