from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

def bfs(a, b):
    distance = [-1] * (n + 1)
    distance[a] = 0
    q = deque([a])

    while q:
        node = q.popleft()
        for i, j in graph[node]:
            if distance[i] == -1:
                distance[i] = distance[node] + j
                q.append(i)
                
    return distance[b]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

for i in range(m):
    start, end = map(int, input().split())
    print(bfs(start, end))
