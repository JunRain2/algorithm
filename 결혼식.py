from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited  = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    
    graph[a].append(b)
    graph[b].append(a)


visited[1] = True
q = deque([1])    

result = 0
while q:
    x = q.popleft()
    for i in graph[x]:
        if not visited[i]:
            visited[i] = True
            if 1 in graph[i]:
                q.append(i)
            result += 1

print(result)
