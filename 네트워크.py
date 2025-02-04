from collections import deque

def bfs(start, visited, graph):
    q = deque([start])
    visited[start] = True
    
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    graph = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(i + 1, n):
            if computers[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)
                
    
    for i in range(n):
        if not visited[i]:
            answer += 1     
            bfs(i, visited, graph)
    return answer