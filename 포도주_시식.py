n = int(input())
array = [0] * (n + 1)
for i in range(1, n + 1):
    array[i] = int(input())

dp = [0] * (n + 1)
dp[1] = array[1]
if n > 1:
    dp[2] = max(array[2], array[1] + array[2])

# 시작이랑 끝이 자유로움
for i in range(3, n + 1):
    dp[i] = max(
        dp[i - 1],  # 마시지 않는 경우
        dp[i - 2] + array[i],  # 두칸 전꺼
        dp[i - 3] + array[i - 1] + array[i],  # 한칸 전꺼
    )

print(dp[n])
