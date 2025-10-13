# 낙하한 지역을 중심으로 거리가 수색범위 m 이내의 모든 지역의 아이템을 습득 가능
# 습득 가능 아이템의 최대개수

INF = int(1e9)

n, m, r = map(int, input().split())
items = list(map(int, input().split()))
graph = [[INF] * n for _ in range(n)]

for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = c
    graph[b-1][a-1] = c
    
# 플로이드 워셜
for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            
result = 0
for i in range(n):
    t = items[i]
    for j in range(n):
        if i == j:
            continue
        
        if graph[i][j] <= m:
            t += items[j]
    
    result = max(result, t)

print(result)