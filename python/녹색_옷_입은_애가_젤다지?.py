import heapq
INF = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
    
cnt = 1
while True:
    n = int(input())
    if n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    distance = [[INF] * n for _ in range(n)]
    
    q = [(graph[0][0], 0, 0)]
    distance[0][0] = graph[0][0]
    
    while q:
        cost, x, y = heapq.heappop(q)
        if distance[x][y] < cost:
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] + cost < distance[nx][ny]:
                    distance[nx][ny] = graph[nx][ny] + cost
                    heapq.heappush(q, (distance[nx][ny], nx, ny))
                
                
    print(f"Problem {cnt}: {distance[n - 1][n - 1]}")
    cnt += 1
    