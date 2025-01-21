from collections import deque


def bfs(array):
    q = deque()
    q.append((0, 0))
    array[0][0] = 1  # 출발, 끝점을 포함

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and array[nx][ny] == 0:
                q.append((nx, ny))
                array[nx][ny] = array[x][y] + 1

    return array[n - 1][m - 1]


n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int, input())))  # 0 이동 가능 / 1 이동 불가


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = int(1e9)
blocks = []
for i in range(n):
    for j in range(m):
        if array[i][j] == 1:
            array[i][j] = 0
            tmp = bfs(array)
            array[i][j] = 1
            if tmp == 0:
                continue
            else:
                result = min(result, tmp)

if result == int(1e9):
    print(-1)
else:
    print(result)
