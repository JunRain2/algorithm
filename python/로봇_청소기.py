n, m = map(int, input().split())
r, c, d = map(int ,input().split())
# 0인 경우, 청소되지 않은 빈칸, 1인 경우 벽이 있는 것
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = 0
x, y = r, c
while True:
    if graph[x][y] == 0:
        graph[x][y] = -1
        answer += 1
    
    flag = True
    for i in range(4):
        direct = (d + i) % 4
        nx, ny = x + dx[direct], y + dy[direct]
        # 벽이 아니고 청소가 안된 경우
        if graph[nx][ny] == 0:
            flag = False
            break
        
    # 모든 칸이 청소된 경우
    if flag:
        nx, ny = x - dx[d], y - dy[d]
        # 뒤가 벽인 경우
        if graph[nx][ny] == 1:
            print(answer)
            exit()
        x, y = nx, ny
    # 모든 칸이 청소되어 있지 않은 경우
    else:
        d = (d - 1) % 4
        nx, ny = x + dx[d], y + dy[d]
        if graph[nx][ny] == 0:
            x, y = nx, ny