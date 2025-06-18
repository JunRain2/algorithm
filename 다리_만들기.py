from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def find_island(x, y, cnt):
    q = deque([(x, y)])
    graph[x][y] = cnt

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = cnt


cnt = 2
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            find_island(i, j, cnt)
            cnt += 1

def bfs(x, y, visited, island_cnt):
    q = deque([(x, y)])
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if graph[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

                elif graph[nx][ny] != island_cnt:
                    return visited[x][y]

    return int(1e9)


result = int(1e9)
for i in range(n):
    for j in range(n):
        if graph[i][j] >= 2:
            for k in range(4):
                visited = [[0] * n for _ in range(n)]
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                    result = min(result, bfs(nx, ny, visited, graph[i][j]))

print(result)
