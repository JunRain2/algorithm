import heapq

INF = int(1e9)

def dijkstra(start, graph, n):
    distance = [INF] * (n + 1)
    distance[start] = 0
    q = [(0, start)]
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for b, c in graph[now]:
            cost = dist + c
            if distance[b] > cost:
                distance[b] = cost
                heapq.heappush(q, (cost, b))
                
    return distance
                
# 지점의 개수, 출발지, A의 도착지, B의 도착지, 
def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]
    
    for x, y, c in fares:
        graph[x].append((y, c))
        graph[y].append((x, c))
        
    distance = dijkstra(s, graph, n)
    answer = distance[a] + distance[b]
    
    for i in range(n + 1):
        dist = dijkstra(i, graph, n)
        answer = min(answer, distance[i] + dist[a] + dist[b])
    
    return answer