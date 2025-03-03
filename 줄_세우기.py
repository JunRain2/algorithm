from collections import deque

# n명의 학생, m번 비교
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
indegrees = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegrees[b] += 1

q = deque()
result = []
for i in range(1, n + 1):
    if indegrees[i] == 0:
        q.append(i)

while q:
    v = q.popleft()
    result.append(v)
    
    for i in graph[v]:
        indegrees[i] -= 1
        if indegrees[i] == 0:
            q.append(i)

print(*result)