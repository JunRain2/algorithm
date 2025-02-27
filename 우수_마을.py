from collections import deque

# 트리구조, 무방향
n = int(input())
v = [0] + list(map(int, input().split())) # 주민 수
graph = [[] for _ in range(n + 1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(start, visited):
    q = deque([start])
    check = [False] * (n + 1)
    check[start] = True
    cnt = v[start]
    visited[start] = True
    
    while q:
        node = q.popleft()
        for i in graph[node]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                check[i] = not check[node]
                if check[i]:
                    cnt += v[i]
        
    return cnt

result = 0

for i in range(1, n + 1):
    visited = [False] * (n + 1)
    result = max(result, bfs(i, visited))
    
print(result)