m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]

# dp 배열을 (m+1) x (n+1) 크기로 만들어서 인덱스 에러를 방지합니다.
dp = [[0] * (n + 1) for _ in range(m + 1)]
result = 0

# 1부터 시작하는 이유는 dp 배열의 첫 행, 첫 열을 0으로 두고
# graph의 인덱스와 dp를 맞추기 위함입니다.
for i in range(1, m + 1):
    for j in range(1, n + 1):
        # graph의 인덱스는 0부터 시작하므로 i-1, j-1을 사용합니다.
        if graph[i - 1][j - 1] == 0:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            result = max(result, dp[i][j])
            
print(result)