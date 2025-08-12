n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]


def calculate_min_cost(start_color):
    dp = [[int(1e9)] * 3 for _ in range(n)]
    dp[0][start_color] = costs[0][start_color]

    for i in range(1, n):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]

    return min(dp[-1][(start_color + 1) % 3], dp[-1][(start_color + 2) % 3])


result = min(calculate_min_cost(0), calculate_min_cost(1), calculate_min_cost(2))
print(result)
