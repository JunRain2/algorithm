from collections import deque

dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [1, -1, 0, 1, -1, 0, 1, -1]

def bfs(graph, w, h, x, y, visited):
    q = deque([(x, y)])
    visited[x][y] = True
    
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and graph[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] += 1
        
    

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    
    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    
    cnt = 0
    for x in range(h):
        for y in range(w):
            if graph[x][y] == 1 and not visited[x][y]:
                bfs(graph, w, h, x, y, visited)
                cnt += 1
                
    print(cnt)
    
    