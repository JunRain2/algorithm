# 카드 N개가 포함된 N가지 카드팩
# 돈을 많이 써서 N개의 카드팩을 구매
n = int(input())
array = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(1, n + 1):
    tmp = [array[i]]
    for j in range(1, i):
        tmp.append(dp[i - j] + array[j])
    dp[i] = max(tmp)
    
print(dp[n])