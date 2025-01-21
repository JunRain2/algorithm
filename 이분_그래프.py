from collections import deque

for tc in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    flag = True
    visited = [-1] * (v + 1)
    for start in range(1, v + 1):
        if visited[start] == -1:
            q = deque([start])
            visited[start] = 0
            while q and flag:
                v = q.popleft()
                for i in graph[v]:
                    if visited[i] == -1:
                        visited[i] = 1 - visited[v]
                        q.append(i)
                    elif visited[i] == visited[v]:
                        flag = False
                        break

    if not flag:
        print("NO")
    else:
        print("YES")
