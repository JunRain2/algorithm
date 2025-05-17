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
q = deque([(1, 0)])    

result = 0
while q:
    x, depth = q.popleft()
    for i in graph[x]:
        if not visited[i] and depth < 2:
            visited[i] = True
            result += 1
            q.append((i, depth + 1))

print(result)
