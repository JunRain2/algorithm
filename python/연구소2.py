from itertools import combinations
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def check(visited):
    for i in range(n):
        for j in range(n):
            if array[i][j] == 1:
                continue
            elif visited[i][j] == 0:
                return False
    return True


def bfs(virus):
    visited = [[0] * n for _ in range(n)]
    for x, y in virus:
        visited[x][y] = 1

    q = deque(virus)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < n
                and 0 <= ny < n
                and array[nx][ny] == 0
                and visited[nx][ny] == 0
            ):
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
                
    if check(visited):
        return max(map(max, visited)) - 1
    return int(1e9)


n, m = map(int, input().split())  # n*n 바이러스 개수
array = []
virus = []
for i in range(n):
    data = list(map(int, input().split()))
    array.append(data)
    for j in range(n):
        if data[j] == 2:
            virus.append((i, j))
            array[i][j] = 0

result = int(1e9)
for i in combinations(virus, m):
    result = min(result, bfs(i))

if result == int(1e9):
    print(-1)
else:
    print(result)
