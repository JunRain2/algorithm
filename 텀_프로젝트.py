for tc in range(int(input())):
    n = int(input())
    visited = [0] * n
    graph = list(map(int, input().split()))
    
    def dfs(v, cnt):
        if visited[v]:
            if visited[v] == 1:
                return cnt, graph[v] - 1
            else:
                return 0
        visited[v] = 1
        result = dfs(graph[v] - 1, cnt + 1)
        visited[v] = 2
        return result
    
    answer = n
    for i in range(n):
        if not visited[i]:
            answer -= dfs(i, 0)
    print(answer)