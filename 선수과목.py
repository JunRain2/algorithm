from collections import deque

# 모든 과목을 이수해야만 해당 과목을 이수
# 과목의 수, 선수 조건의 수
n, m = map(int, input().split())
distance = [1] * n
indegrees = [0] * (n + 1)

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegrees[b] += 1

q = deque()
for i in range(1, n + 1):
    if indegrees[i] == 0:
        q.append(i)
        
while q:
    v = q.popleft()
    
    for i in graph[v]:
        distance[i - 1] = distance[v - 1] + 1
        indegrees[i] -= 1
        if indegrees[i] == 0:
            q.append(i)
    
print(*distance)