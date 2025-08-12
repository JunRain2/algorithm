import sys
sys.setrecursionlimit(10**5)

def dfs(v, visited):
    visited[v] = True
    cnt = 0
    for i in graph[v]:
        if not visited[i]:
            cnt += dfs(i, visited)
    return cnt + 1

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
    
x = int(input())
visited = [False] * (n + 1)

print(dfs(x, visited) - 1)