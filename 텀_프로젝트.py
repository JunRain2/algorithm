import sys
sys.setrecursionlimit(10**5)

for tc in range(int(input())):
    n = int(input())
    array = [0] + list(map(int, input().split()))
    
    def dfs(v, route):
        if visited[v]:
            if v not in route:
                return 0
            else:
                return len(route[route.index(v):])
        
        visited[v] = True
        route.append(v)
        return dfs(array[v], route)
    
    result = n
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        if not visited[i]:
            result -= dfs(i, [])
    
    print(result)