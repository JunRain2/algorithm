from collections import deque

n, m, k, x = map(int, input().split())

visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

result = list()


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    count = 0
    while queue:
        v = queue.popleft()

        count += 1
        for i in graph[v]:
            if not visited[i]:
                if count == k:
                    result.append(i)
                queue.append(i)
                visited[i] = True
        if count == k:
            return


bfs(graph, x, visited)

result.sort()
if result:
    for i in result:
        print(i)
else:
    print(-1)
