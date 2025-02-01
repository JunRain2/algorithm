dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

graph = []  # 상어를 17로 둠
for i in range(4):
    data = list(map(int, input().split()))
    input_data = []
    for j in range(0, 8, 2):
        input_data.append((data[j], data[j + 1] - 1))
    graph.append(input_data)


def search_fish(num):
    for i in range(4):
        for j in range(4):
            if graph[i][j][0] == num:
                return i, j
    return None


def swap_fish():
    for i in range(1, 17):
        fish = search_fish(i)
        if fish == None:
            continue
        # 전진 할 곳이 없거나, 상어가 있으면 반시계 방향으로 돌림
        nx = ny = -1
        while True:
            direct = graph[fish[0]][fish[1]][1]
            nx, ny = (
                fish[0] + dx[direct],
                fish[1] + dy[direct],
            )
            if 0 <= nx < 4 and 0 <= ny < 4 and graph[nx][ny][0] != 17:
                break
            graph[fish[0]][fish[1]] = (graph[fish[0]][fish[1]][0],(direct + 1) % 8)
        graph[fish[0]][fish[1]], graph[nx][ny] = graph[nx][ny], graph[fish[0]][fish[1]]


def forward_shark(result):
    shark = search_fish(17)
    direct = graph[shark[0]][shark[1]][1]
    nx, ny = shark[0], shark[1]
    tmp = []
    for _ in range(3):
        nx += dx[direct]
        ny += dy[direct]
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4 or graph[nx][ny] == -1:
            continue
        tmp.append((graph[nx][ny][0], nx, ny))

    if len(tmp) == 0:
        print(result)
        exit()
    tmp.sort()
    cost, nx, ny = tmp[-1]

    graph[shark[0]][shark[1]] = (-1, -1)
    graph[nx][ny] = (17, graph[nx][ny][1])

    return cost


result = graph[0][0][0]
graph[0][0] = (17, graph[0][0][1])
for _ in range(16):
    swap_fish()
    result += forward_shark(result)

print(result)
