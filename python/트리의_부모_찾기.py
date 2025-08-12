from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
q = deque([1])
visited[1] = True

result = [0] * (n + 1)
while q:
    node = q.popleft()
    for i in graph[node]:
        if not visited[i]:
            q.append(i)
            result[i] = node
            visited[i] = True
            
for i in range(2, n + 1):
    print(result[i])