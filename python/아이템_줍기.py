from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    graph = [[-1] * 101 for _ in range(101)]
    distance = [[-1] * 101 for _ in range(101)]
    
    for r in rectangle:
        lx, ly, rx, ry = map(lambda x: x * 2, r)
        for i in range(lx ,rx + 1):
            for j in range(ly, ry + 1):
                if lx < i < rx and ly < j < ry:
                    graph[i][j] = 0
                elif graph[i][j] != 0:
                    graph[i][j] = 1
                
                    
    q = deque([(characterX * 2, characterY * 2)])
    distance[characterX * 2][characterY * 2] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= 100 and 0 <= ny <= 100 and distance[nx][ny] == -1 and graph[nx][ny] == 1:
                distance[nx][ny] = distance[x][y] + 1
                q.append((nx, ny))
                    
    return distance[itemX * 2][itemY * 2] // 2 