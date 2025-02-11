from collections import deque

dx = [1, 0]
dy = [0, 1]

def dfs(short_value, graph, x, y, n, m, distance):
    if x == (n - 1) and y == (m - 1):
        if distance == short_value:
            return 1
        else:
            return 0
    if x < 0 or x >= n or y < 0 or y >= m or graph[x][y] == 1 or distance > short_value:
        return 0
    
    cnt = 0
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        cnt += dfs(short_value, graph, nx, ny, n, m, distance + 1)
        
    return cnt

def solution(m, n, puddles):
    answer = 0
    
    graph = [[0] * m for i in range(n)]
    distance = [[-1] * m for i in range(n)]
    
    for x, y in puddles:
        graph[x -1][y - 1] = 1
    
    q = deque([(0, 0)])
    distance[0][0] = 0
    while q:
        x, y = q.popleft()
        
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and distance[nx][ny] == -1 and graph[nx][ny] != 1:
                distance[nx][ny] = distance[x][y] + 1
                q.append((nx, ny))
    
    return dfs(distance[n - 1][m - 1], graph, 0, 0, n, m, 0) % 1000000007