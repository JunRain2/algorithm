# 중점(0), 위(1), 왼쪽(2), 아래(3), 오른쪽(4)
# 시작은 중점, 한 번에 한 발만 움직여야 함
# 게임 시작을 제외하고 두 발이 같이 있어서는 안됨


arr = list(map(int, input().split()))

arr = arr[: len(arr) - 1]
n = len(arr)


# 힘의 크기가 다 다름
# 같은 지점 -> 1
# 중앙에서 이동 -> 2
# 인접(왼 -> 위 / 왼 -> 오) -> 3
# 반대(왼 -> 오 / 위 -> 아) -> 4
def add_power(s, e):
    if s == e:
        return 1
    elif s == 0:
        return 2
    elif abs(e - s) == 2:
        return 4
    return 3


# 현재 위치 = min(현재 위치, 왼발 움직였을 때, 오른발 움직였을 때)
INF = int(1e9)
dp = [[[INF] * 5 for _ in range(5)] for _ in range(n + 1)]
dp[0][0][0] = 0

for i in range(n):
    for left in range(5):
        for right in range(5):
            if dp[i][left][right] == INF:
                continue

            if right != arr[i]:
                dp[i + 1][arr[i]][right] = min(
                    dp[i + 1][arr[i]][right],
                    dp[i][left][right] + add_power(left, arr[i]),
                )

            if left != arr[i]:
                dp[i + 1][left][arr[i]] = min(
                    dp[i + 1][left][arr[i]],
                    dp[i][left][right] + add_power(right, arr[i]),
                )

result = INF
for left in range(5):
    for right in range(5):
        result = min(result, dp[n][left][right])

print(result)
