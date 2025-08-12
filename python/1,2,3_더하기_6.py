dp = [0, 1, 2, 2, 3, 3, 6]
for i in range(7, 100001):
    dp.append((dp[i - 2] + dp[i - 4] + dp[i - 6]) % 1000000009)


for tc in range(int(input())):
    print(dp[int(input())])
