# n*n 격자
# 바구니에 저장할 수 있는 물의 양은 제한 X
# (1, 1) ~ (N * N) 1번 행·열 과 N번 행·열과 연결
# 비바라기 시전 (N, 1), (N, 2), (N - 1, 1), (N - 1, 2)에 비구름

# 1, 3, 5, 7 -> 대각선
import copy

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


# 구름 생성
def create(prev):
    cloud = []

    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 2 and (i, j) not in prev:
                graph[i][j] -= 2
                cloud.append((i, j))

    return cloud


def move(cloud, d, s):
    result = []
    d -= 1

    for x, y in cloud:
        nx = (x + (dx[d] * s)) % n
        ny = (y + (dy[d] * s)) % n

        result.append((nx, ny))

    return result


def bug(cloud):
    tmp = copy.deepcopy(graph)

    for x, y in cloud:
        for i in range(1, 8, 2):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > 0:
                tmp[x][y] += 1

    return tmp


# 이전 구름의 위치
cloud = {(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)}
for _ in range(m):
    d, s = map(int, input().split())

    # 1. 구름 이동
    cloud = move(cloud, d, s)
    # 2. 구름이 있는 칸 +1
    for x, y in cloud:
        graph[x][y] += 1

    # 4. 물복사 버그 시전, 대각선 방향으로 가리가 1인 칸에
    #   물이 있는 바구니 수 만큼 (r, c)에 있는 바구니의 물의 양이 증가
    # 경계를 넘어가는 칸은 X
    graph = bug(cloud)

    # 5. 바구니에 저장된 물의 양이 2 이상인 칸에 구름이 생성되고, 물의 양이 2 줄어든다.
    # 구름이 생성되는 칸은 3번에서 구름이 사라진 칸이 아니어야 함
    cloud = create(cloud)

print(sum(map(sum, graph)))
