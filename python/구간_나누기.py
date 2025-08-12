n, m = map(int, input().split())
array = [int(input()) for _ in range(n)]

ps = [0] * (n + 1)
for i in range(1, n + 1):
    ps[i] = ps[i - 1] + array[i - 1]

dp = [[0] * (m + 1) for _ in range(n + 1)]
visited = [[False] * (m + 1) for _ in range(n + 1)]

def range_split(r, s):
    if s == 0:
        return 0
    if r <= 0:
        return -3276800
    if visited[r][s]:
        return dp[r][s]
    
    visited[r][s] = True
    dp[r][s] = range_split(r - 1, s)
    
    for i in range(r, 0, -1):
        dp[r][s] = max(dp[r][s], range_split(i - 2, s - 1) + ps[r] - ps[i - 1])
    
    return dp[r][s]

print(range_split(n, m))
