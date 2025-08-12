import sys

input = sys.stdin.readline
INF = int(1e9)

def bellman_ford(start):
    dist = [INF] * (N + 1)
    dist[start] = 0
    
    for i in range(N):
        for cur, next, cost in edges:
            if dist[cur] != INF and dist[next] > dist[cur] + cost:
                dist[next] = dist[cur] + cost
                if i == N - 1:  # N번째 반복에서 갱신이 일어나면 음의 사이클 존재
                    return True
    
    return dist

# 입력 처리
N, M = map(int, input().split())
edges = []
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))

# 벨만-포드 알고리즘 실행
negative_cycle = bellman_ford(1)

if negative_cycle == True:
    print(-1)
else:
    for i in range(2, N + 1):
        if negative_cycle[i] == INF:
            print(-1)
        else:
            print(negative_cycle[i])
