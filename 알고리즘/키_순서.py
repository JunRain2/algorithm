INF = int(1e9)

n, m = map(int, input().split())
distance = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    distance[i][i] = 0

for i in range(m):
    a, b = map(int, input().split())
    distance[a][b] = 1


for k in range(1, n + 1):
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            distance[x][y] = min(distance[x][y], distance[x][k] + distance[k][y])

result = 0 
# 자기보다 키 큰 사람과 작은 사람을 모두 알 수 있음         
for i in range(1, n + 1):
    cnt = 0
    for j in range(1, n + 1):
        # 자기보다 큰 경우 or 자기보다 작은 경우를 모두 아는 경우
        if distance[i][j] != INF or distance[j][i] != INF:
            cnt += 1
    if cnt == n:
        result += 1

print(result)