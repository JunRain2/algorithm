from collections import deque

n = int(input())  # 도시
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
m = int(input())  # 도로

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    indegree[b] += 1

start, end = map(int, input().split())  # 출발 도시, 도착 도시

dp = [[] for _ in range(n + 1)]
parent = list(range(n + 1))  # 백트래킹을 위한 배열
q = deque([start])
while q:
    v = q.popleft()
    for b, cost in graph[v]:
        indegree[b] -= 1
        if dp[v]:
            for i in dp[v]:
                dp[b].append(i + cost)
        else:
            dp[b].append(cost)
        if indegree[b] == 0:
            q.append(b)

print(max(dp[end]))
cnt = 0
for i in dp[end]:
    if i == max(dp[end]):
        cnt += 1

print(cnt)
