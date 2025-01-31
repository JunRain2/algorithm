from collections import deque

for tc in range(int(input())):
    n, k = map(int, input().split())  # 건물의 수, 건설 규칙
    graph = [[] for _ in range(n + 1)]
    cost = list(map(int, input().split()))
    cost = [0] + cost
    indegree = [0] * (n + 1)
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    w = int(input()) # 승리하기 위해 건설해야 하는 번호 
    q = deque()
    result = [0] * (n + 1)
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            result[i] = cost[i]

    while q:
        v = q.popleft()
        for i in graph[v]:
            indegree[i] -= 1
            result[i] = max(result[i], result[v] + cost[i])
            if indegree[i] == 0:
                q.append(i)
                
    print(result[w])
