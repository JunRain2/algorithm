from collections import deque


def check_result():
    for i in range(n):
        for j in range(m):
            if array[i][j] == 0:
                return False
    return True


def bfs(data):
    q = deque()
    for x, y in data:
        q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and array[nx][ny] == 0:
                array[nx][ny] = array[x][y] + 1
                q.append((nx, ny))


m, n = map(int, input().split())  # 가로 칸, 세로 칸
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))


# 1은 익은 토마토, 0은 익지 않은 토마토, -1은 토마토가 없음
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
result = 0

data = []
for i in range(n):
    for j in range(m):
        if array[i][j] == 1:
            data.append((i, j))

bfs(data)

if check_result():
    print(max(map(max, array)) - 1) # 2차원 배열 최댓값 찾는 방법
else:
    print(-1)
