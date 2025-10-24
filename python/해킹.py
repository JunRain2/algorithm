import heapq

INF = int(1e9)

for _ in range(int(input())):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(d):
        a, b, cost = map(int, input().split())
        graph[b].append((a, cost))

    visited = [INF] * (n + 1)
    visited[c] = 0
    q = [(0, c)]

    while q:
        dist, now = heapq.heappop(q)
        if dist > visited[now]:
            continue
        for i, c in graph[now]:
            cost = visited[now] + c
            if visited[i] > cost:
                visited[i] = cost
                heapq.heappush(q, (cost, i))

    result = 0
    cnt = 0
    for i in range(1, n + 1):
        # INF일 경우 오염되지 않은 컴퓨터라는 의미
        if visited[i] < INF:
            # 제일 오래 걸린 컴퓨터 -> 제일 마지막에 감연된 컴퓨터
            result = max(result, visited[i])
            cnt += 1

    print(cnt, result)
