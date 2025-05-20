from collections import deque

n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(k):
    a, b, c = map(int, input().split())
    if b < a:
        continue

    graph[a].append((b, c))

dp = [0] * (n + 1)

q = deque([(1, 1)])
while q:
    node, depth = q.popleft()

    if depth < m:
        for b, c in graph[node]:
            dp[b] = max(dp[b], dp[node] + c)
            q.append((b, depth + 1))

print(dp[n])
