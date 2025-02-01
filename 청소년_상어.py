import copy

result = 0

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

graph = [[None] * 4 for _ in range(4)]
for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        graph[i][j] = [data[j * 2], data[(j * 2) + 1] - 1]


def search_fish(graph, num):
    for i in range(4):
        for j in range(4):
            if graph[i][j][0] == num:
                return i, j
    return None


def swap_fish(graph, x, y):
    for i in range(1, 17):
        fish = search_fish(graph, i)
        if fish != None:
            fx, fy = fish
            direction = graph[fx][fy][1]
            for _ in range(8):
                nx = fx + dx[direction]
                ny = fy + dy[direction]
                if 0 <= nx < 4 and 0 <= ny < 4:
                    if not (nx == x and ny == y):
                        graph[fx][fy][1] = direction
                        graph[fx][fy], graph[nx][ny] = (
                            graph[nx][ny],
                            graph[fx][fy],
                        )
                        break
                direction = (direction + 1) % 8


def forward_shark(graph, x, y):
    direction = graph[x][y][1]
    tmp = []
    for _ in range(4):
        x += dx[direction]
        y += dy[direction]
        if 0 <= x < 4 and 0 <= y < 4:
            if graph[x][y][0] != -1:
                tmp.append((x, y))
    return tmp


def dfs(array, x, y, total):
    global result
    array = copy.deepcopy(array)

    total += array[x][y][0]
    array[x][y][0] = -1

    swap_fish(array, x, y)
    positions = forward_shark(array, x, y)
    
    if len(positions) == 0:
        result = max(result, total)
        return

    for nx, ny in positions:
        dfs(array, nx, ny, total)


dfs(graph, 0, 0, 0)
print(result)
