# n개의 앱, 확보해야하는 메모리
n, m = map(int, input().split())

# 현재 활성화 되어있는 앱이 사용중인 메모리의 바이트 수
a = [0] + list(map(int, input().split()))
# 앱을 비활성화 했을 경우의 비용
c = [0] + list(map(int, input().split()))

# 활성화 되어있는 앱들 중 몇 개를 선택하여 메모리로부터 삭제
# 가치는 무게
dp = [[0] * (sum(c) + 1) for _ in range(n + 1)]

result = sum(c) + 1
for i in range(1, n + 1):
    w, v = c[i], a[i]
    for j in range(sum(c) + 1):
        if w > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
            if dp[i][j] >= m:
                result = min(result, j)
            
print(result)