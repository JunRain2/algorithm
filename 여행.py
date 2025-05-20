n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(k):
    a, b, c = map(int, input().split())
    if b > a:
        graph[a].append((b, c))

dp = [[-1] * (m + 1) for _ in range(n + 1)]
dp[1][1] = 0  # 시작점

for i in range(1, m):
    for u in range(1, n + 1):
        if dp[u][i] == -1:
            continue
        for v, cost in graph[u]:
            if dp[v][i + 1] < dp[u][i] + cost:
                dp[v][i + 1] = dp[u][i] + cost

print(max(dp[n]))