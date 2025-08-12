from collections import deque

n, k = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int, input().split()))[:n])

s, x, y = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

list = []
for i in range(n):
    for j in range(n):
        if array[i][j] != 0:
            list.append((array[i][j], i, j))

list.sort()
q = deque(list)

for _ in range(s):
    tmp = []
    while q:
        c, a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n and array[nx][ny] == 0:
                array[nx][ny] = c
                tmp.append((c, nx, ny))

    q = deque(tmp)


print(array[x - 1][y - 1])