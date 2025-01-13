from collections import deque

n, l, r = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

array = list()

for _ in range(n):
    array.append(list(map(int, input().split()))[:n])

result = [[0] * n for _ in range(n)]


# bfs를 통해서 연합을 나눔
def bfs(start, cnt):
    q = deque([start])
    data = [[0] * n for _ in range(n)]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= 0 and nx < n and ny >= 0 and ny < n and data[nx][ny] == 0:
                tmp = abs(array[x][y] - array[nx][ny])
                if tmp >= l and tmp <= r:
                    data[nx][ny] = cnt
                    q.append((nx, ny))
    
    return data

# 연합을 이루는 있는 각 칸의 인구수 계산
def sum(data, array):
    for i in range(n):
        for j in range(n):
            


print(result)
