n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
orders = list(map(int, input().split()))

# 동, 서, 북, 남의 이동 방향 (order: 1,2,3,4)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 주사위 상태:
# dice[1]: 윗면, dice[2]: 북쪽, dice[3]: 동쪽, dice[4]: 서쪽, dice[5]: 남쪽, dice[6]: 바닥면
dice = [0] * 7

for order in orders:
    nx = x + dx[order - 1]
    ny = y + dy[order - 1]

    # 격자 범위 검사 (세로 크기 n, 가로 크기 m)
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

    # 이동한 방향에 따라 주사위의 면 재배치
    if order == 1:  # 동쪽
        dice[1], dice[4], dice[6], dice[3] = dice[4], dice[6], dice[3], dice[1]

    elif order == 2:  # 서쪽
        dice[1], dice[3], dice[6], dice[4] = dice[3], dice[6], dice[4], dice[1]

    elif order == 3:  # 북쪽
        dice[1], dice[5], dice[6], dice[2] = dice[5], dice[6], dice[2], dice[1]

    elif order == 4:  # 남쪽
        dice[1], dice[2], dice[6], dice[5] = dice[2], dice[6], dice[5], dice[1]

    # 새로운 위치로 이동
    x, y = nx, ny

    # 이동한 칸의 값에 따라 복사 작업 수행
    if graph[x][y] == 0:
        graph[x][y] = dice[6]
    else:
        dice[6] = graph[x][y]
        graph[x][y] = 0

    print(dice[1])
