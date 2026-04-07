from collections import deque

dx = [2, 2, 1, -1, -2, -2, -1, 1]
dy = [1, -1, 2, 2, 1, -1, -2, -2]

for _ in range(int(input())):
    i = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    
    visited = [[-1] * i for _ in range(i)]
    q = deque([(start[0], start[1])])
    visited[start[0]][start[1]] = 0
    
    while q:
        x, y = q.popleft()
        
        for j in range(8):
            nx, ny = x + dx[j], y + dy[j]
            if 0 <= nx < i and 0 <= ny < i and visited[nx][ny] == -1:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                
        if visited[end[0]][end[1]] != -1:
            print(visited[end[0]][end[1]])
            break