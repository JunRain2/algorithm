n, m = map(int, input().split())
company =[[0] for _ in range(m + 1)]

for _ in range(n):
    data = list(map(int, input().split()))
    for i in range(1, m + 1):
        company[i].append(data[i])
        
parent = [[0] * (n + 1) for _ in range(m + 1)]
        
dp = [[0] * (n + 1) for _ in range(m + 1)]
for i in range(1, m + 1):
    for j in range(1, n + 1):
        for k in range(0, j + 1):
            if dp[i][j] < dp[i - 1][j - k] + company[i][k]:
                dp[i][j] = dp[i-1][j - k] + company[i][k]
                parent[i][j] = k

print(dp[m][n])

result = []
t = n
prev = parent[m]
for i in range(m, 0, -1):
    result.append(parent[i][t])
    t -= parent[i][t]

print(*reversed(result))