n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
orders = list(map(int, input().split()))

# 동, 서, 북, 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면,주사위의 바닥면에 쓰여 있는 수가 복사
# 0이 아닌 경우, 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사, 칸에 쓰여있는 수는 0

dice = [0] * 7
current = 1
# 동, 서, 북, 남, 반대
dices = [
    [],
    [3, 4, 2, 5, 6],  # 1
    [3, 4, 6, 1, 5],  # 2
    [6, 1, 2, 5, 4],  # 3
    [1, 6, 2, 5, 3],  # 4
    [3, 4, 1, 6, 2],  # 5
    [3, 4, 5, 2, 1],  # 6
]
for order in orders:
    nx, ny = x + dx[order - 1], y + dy[order - 1]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    current = dices[current][order - 1]
    x, y = nx, ny
    if graph[x][y] == 0:
        graph = dice[dices[current][4]]
    elif dice[dices[current][4]] == 0:
        dice[dices[current][4]] = graph[x][y]
    
    print(dice[current])