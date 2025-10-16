import heapq

# (r, c)는 1부터 시작

# M개의 나무를 사서 심음 -> 1*1 크기에 칸에 여러 개의 나무가 존재할 수 있다.

n, m, k = map(int, input().split())

nour = [list(map(int, input().split())) for _ in range(n)]

# 가장 처음에 양분은 모든 칸에 5만큼 들어가있다.
land = [[5] * n for _ in range(n)]

trees = []

for _ in range(m):
    x, y, z = map(int, input().split())
    heapq.heappush(trees, (z, x - 1, y - 1))


# 봄에는 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가
# 나무가 있는 1*1 크기의 칸에 양분만 먹을 수 있다.
# 하나에 칸에 여러 개의 나무가 있다면 어린 나무부터 양분을 먹는다.
# 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 죽는다.
def spring(trees):
    result = []
    die = []

    while trees:
        age, x, y = heapq.heappop(trees)
        if land[x][y] - age < 0:
            die.append((age, x, y))
        else:
            land[x][y] -= age
            heapq.heappush(result, (age + 1, x, y))

    return result, die


# 여름에는 봄에 죽은 나무가 양분으로 변한다.
# 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가
def summer(die):
    for age, x, y in die:
        land[x][y] += age // 2


# 가을에는 나무가 번식
# 나이가 5의 배수이어야 하며, 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
# 땅을 벗어나는 칸에는 나무가 생기지 않는다.
def autumn(trees):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    for age, x, y in trees:
        if age % 5 == 0:
            for i in range(8):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    trees.append((1, nx, ny))


# 겨울에는 양분을 추가
# 각 칸에 추가되는 양분의 양은 입력
def winter():
    for x in range(n):
        for y in range(n):
            land[x][y] += nour[x][y]


for _ in range(k):
    trees, die = spring(trees)
    summer(die)
    autumn(trees)
    winter()

print(len(trees))
