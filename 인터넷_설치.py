import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 나머지 인터넷 선 중 제일 비싼 것
n, p, k = map(int, input().split()) # 학생들 번호, 케이블 선 개수, 꽁자 제공 케이블 선

graph = [[] for _ in range(n + 1)]
for _ in range(p):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
parent = [() for _ in range(n + 1)]
    
distance = [INF] * (n + 1)
q = []
q.append((0, 1))
distance[1] = 0
while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
        continue
    for b, c in graph[now]:
        cost = c + dist
        if cost < distance[b]:
            parent[b] = (now, c)
            distance[b] = cost
            heapq.heappush(q, (cost, b))
            
if distance[n] < INF:
    x = n
    result = []
    while x != 1:
        index, cost = parent[x]
        x = index
        result.append(cost)
    result.sort(reverse=True)
    print(result[k])
    
else:
    print(-1)