from collections import deque

n, m, s = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
    graph[a].append(b)


q = deque([s])
visited[s] = 1
cnt = 2

while q:
    v = q.popleft()
    graph[v].sort(reverse=True)

    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = cnt
            cnt += 1
            q.append(i)

for i in range(n):
    print(visited[i + 1])
