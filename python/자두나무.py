t, w = map(int, input().split())
array = []
for _ in range(t):
    array.append(int(input()))

w = w + 1
dp = [[0] * w for _ in range(t)]

if array[0] == 1:
    dp[0][0] = 1
else:
    dp[0][1] = 1

for i in range(1, t):
    # 한 번도 안옮겼다 -> 1번 나무 아래
    if array[i] == 1:
        dp[i][0] = dp[i - 1][0] + 1
    else:
        dp[i][0] = dp[i - 1][0]

    for j in range(1, w):
        current = (j % 2) + 1
        # 바꿨을 경우 더 많은가? 바꾸지 않았을 경우가 더 많은가?
        if array[i] == current:
            dp[i][j] = max(dp[i - 1][j] + 1, dp[i - 1][j])
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + 1)

print(max(dp[t - 1]))
