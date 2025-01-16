from collections import deque

for tc in range(int(input())):
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    grades = list(map(int, input().split()))
    for i in range(len(grades) - 1):
        x, y = grades[i], grades[i + 1]
        graph[x].append(y)
        indegree[y] += 1

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    # 위상 알고리즘
    q = deque()
    result = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    if len(result) == n:
        for i in result:
            print(i, end=" ")
    else:
        print("IMPOSSIBLE")
