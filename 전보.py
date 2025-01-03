INF = int(1e9)

n, m, c = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b, j = map(int, input().split())
    graph[a][b] = j

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

count = 0
sum = list()
for i in graph[c]:
    if i == INF or i == 0:
        continue
    count += 1
    sum.append(i)

print(count, max(sum)) # 제일 오래 걸린 시간 기준 반환
