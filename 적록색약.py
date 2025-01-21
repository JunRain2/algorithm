from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

rg_array = ['R', 'G']

def bfs(a, b):
    q = deque()
    q.append((a, b))
    color = array[a][b]
    while q:
        x, y = q.popleft()
        if array[x][y] in rg_array:
            array[x][y] = "RG"
        else:
            array[x][y] = "L"
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and array[nx][ny] == color:
                q.append((nx, ny))

def rg_bfs(a, b):
    q = deque()
    q.append((a, b))
    color = array[a][b]
    while q:
        x, y = q.popleft()
        array[x][y] = "K"
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and array[nx][ny] == color:
                q.append((nx, ny))


n = int(input())
array = []
for _ in range(n):
    array.append(list(input()))

result = [0, 0]

for i in range(n):
    for j in range(n):
        if array[i][j] != "L" and array[i][j] != "RG":
            bfs(i, j)
            result[0] += 1

for i in range(n):
    for j in range(n):
        if array[i][j] != "K":
            rg_bfs(i, j)
            result[1] += 1


print(*result)
