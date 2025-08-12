from collections import deque

n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
# 일단 빙산의 시작점을 알아야 함


def bfs(i, j, visited):  # 빙산을 탐색하면서 빙산을 녹임
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < n
                and 0 <= ny < m
                and not visited[nx][ny]
                and array[nx][ny] != 0
            ):  # 방문한 적 없으면서 0이 아닐 경우
                q.append((nx, ny))
                visited[nx][ny] = True
            elif array[nx][ny] == 0 and not visited[nx][ny]:
                array[x][y] = max(0, array[x][y] - 1)


cnt = 1
result = -1
while cnt == 1:  # 빙산이 하나라면 계속 반복
    result += 1
    cnt = 0
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if array[i][j] != 0 and not visited[i][j]:
                cnt += 1
                bfs(i, j, visited)


if cnt == 0:
    print(0)
else:
    print(result)
