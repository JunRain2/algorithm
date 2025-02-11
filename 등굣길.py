def solution(m, n, puddles):
    mod = 1000000007
    # dp는 n행 m열의 2차원 배열 (행: 세로, 열: 가로)
    dp = [[0] * m for _ in range(n)]
    
    # puddles 리스트는 (x, y) 형식으로 들어오므로, 
    # 이를 (y-1, x-1)로 바꿔서 dp에서 장애물 위치로 사용한다.
    puddle_set = {(y - 1, x - 1) for x, y in puddles}
    
    dp[0][0] = 1  # 출발점은 무조건 1

    for i in range(n):
        for j in range(m):
            # 만약 이 좌표가 웅덩이라면 경로 수는 0
            if (i, j) in puddle_set:
                dp[i][j] = 0
                continue
            # 시작점이 아닐 경우, 위쪽과 왼쪽에서 오는 경로의 수를 더함
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
            dp[i][j] %= mod

    return dp[n - 1][m - 1]