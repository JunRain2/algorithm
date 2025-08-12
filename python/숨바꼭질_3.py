from collections import deque

n, k = map(int, input().split())

graph = [-1] * 100001
graph[n] = 0

dx = [-1, 1]

q = deque([n])
while q:
    x = q.popleft()
    if x == k:
        break
    nx = x * 2
    if 0 <= nx < 100001 and graph[nx] == -1:
        graph[nx] = graph[x]
        q.append(nx)
    for i in range(2):
        nx = x + dx[i]
        if 0 <= nx < 100001 and graph[nx] == -1:
            graph[nx] = graph[x] + 1
            q.append(nx)

print(graph[k])
