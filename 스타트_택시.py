from collections import deque

INF = int(1e9)

# 손님을 도착지로 데려다 줄 때마다 연료가 충전
# 연료가 바닥나며 업무 종료

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 현재 위치에서 최단거리가 가장 짧은 승객
# 짧은 승객이 여러명이면, 열 번호가 가장 작은 승객

# 모두 다 데려 갈수 있으면, 남은 연료양을 출력

# graph, 승객 수, 연료 양
n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

x, y = map(int, input().split())
x, y = x - 1, y - 1

start = []
end = dict()
for i in range(m):
    sx, sy, ex, ey = map(int, input().split())
    sx, sy, ex, ey = sx - 1, sy - 1, ex - 1, ey - 1
    start.append((sx, sy))
    end[(sx, sy)] = (ex, ey)


def calculate_distance_passengers(x, y):
    visited = [[INF] * n for _ in range(n)]
    q = deque([(x, y)])
    visited[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (
                0 <= nx < n
                and 0 <= ny < n
                and graph[nx][ny] == 0
                and visited[nx][ny] == INF
            ):
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    return visited


def calculate_end(x, y, ex, ey):
    if (x, y) == (ex, ey):
        return 0

    visited = [[INF] * n for _ in range(n)]
    q = deque([(x, y)])
    visited[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (
                0 <= nx < n
                and 0 <= ny < n
                and graph[nx][ny] == 0
                and visited[nx][ny] == INF
            ):
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
                if (nx, ny) == (ex, ey):
                    return visited[nx][ny]
    print(-1)
    exit()


while start:
    distance = calculate_distance_passengers(x, y)

    min_distance = INF
    for sx, sy in sorted(start):
        if min_distance > distance[sx][sy]:
            min_distance = distance[sx][sy]
            x, y = sx, sy

    k -= min_distance
    if k < 0:
        break
    
    ex, ey = end[(x, y)]

    distance = calculate_end(x, y, ex, ey)
    k -= distance

    if k < 0:
        break

    start.remove((x, y))
    x, y = ex, ey
    k += distance * 2

if start:
    print(-1)
else:
    print(k)
