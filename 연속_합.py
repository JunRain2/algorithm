from itertools import combinations

n = int(input())
array = list(map(int, input().split()))

dp = []
dp.append(array[0])
for i in range(1, n):
    s = dp[i - 1] + array[i]
    dp.append(s)

result =  -int(1e9)
for a, b in list(combinations(dp, 2)):
    result = max(result, b - a)

print(result)