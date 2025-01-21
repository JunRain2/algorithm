from collections import deque


def bfs(start):
    q = deque()
    q.append(start)
    array[start[0]][start[1]] = 0
    result = 0
    while q:
        x, y = q.popleft()
        result += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and array[nx][ny] == 1:
                q.append((nx, ny))
                array[nx][ny] = 0
    return result


n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, input())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

result = 0
result_array = []

for i in range(n):
    for j in range(n):
        if array[i][j] == 1:
            result += 1
            result_array.append(bfs((i, j)))

print(result)
result_array.sort()
for i in result_array:
    print(i)
