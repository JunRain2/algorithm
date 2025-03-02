from collections import deque

n, m = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())

graph = [list(input()) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs():
    visited = [[False] * m for _ in range(n)]
    q = deque([(x1 - 1, y1 - 1)])
    while q:
        x, y = q.popleft()
        if x == x2 - 1 and y == y2 - 1:
            return True
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == '1':
                    graph[nx][ny] = '0'
                else:
                    q.append((nx, ny))
                visited[nx][ny] = True
    return False

cnt = 0
while not bfs():
    cnt += 1
    
print(cnt + 1)