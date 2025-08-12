from collections import deque

def bfs(n, m, array):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)] # [x][y][wall] wall == 0이면 벽을 부수지 않고 도달한 거리 1이면 부수고 도달한 거리
    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while queue:
        x, y, wall = queue.popleft() # 좌표, 벽을 부수고 온건지 아닌지 여부
        if x == n - 1 and y == m - 1:
            return visited[x][y][wall]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if array[nx][ny] == 0 and visited[nx][ny][wall] == 0: # 방문하지 않았던 경우
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                    queue.append((nx, ny, wall))
                elif array[nx][ny] == 1 and wall == 0: # 벽을 방문한 경우
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append((nx, ny, 1))

    return -1

n, m = map(int, input().split())
array = [list(map(int, input())) for _ in range(n)]

result = bfs(n, m, array)
print(result)
