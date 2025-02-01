from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
m = int(input())
for _ in range(m):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    indegree[q] += 1

dp = [0] * (n + 1)
queue = deque([1])
path = [[] for _ in range(n + 1)]
path[1] = [1]

while queue:
    v = queue.popleft()
    for q, r in graph[v]:
        indegree[q] -= 1
        if dp[q] < dp[v] + r:
            dp[q] = dp[v] + r
            path[q] = path[v] + [q]
        if indegree[q] == 0:
            queue.append(q)

print(dp[1])
print(*path[1])
