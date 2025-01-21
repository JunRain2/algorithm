from collections import deque

n, m = map(int, input().split())  # 도착점

array = []
for _ in range(n):
    array.append(list(map(int, input())))

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

q = deque()
q.append((0, 0))

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and array[nx][ny] == 1:
            array[nx][ny] = array[x][y] + 1
            q.append((nx, ny))

print(array[n - 1][m - 1])
