for _ in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]

    if n == 1:
        print(max(arr[0][0], arr[1][0]))
        continue

    dp = [[0] * n for _ in range(3)]
    dp[1][0] = arr[0][0]  # 위 고름
    dp[2][0] = arr[1][0]  # 아래 고름

    for i in range(1, n):
        dp[0][i] = max(dp[0][i-1], dp[1][i-1], dp[2][i-1])
        dp[1][i] = max(dp[0][i-1], dp[2][i-1]) + arr[0][i]
        dp[2][i] = max(dp[0][i-1], dp[1][i-1]) + arr[1][i]

    print(max(dp[0][n-1], dp[1][n-1], dp[2][n-1]))