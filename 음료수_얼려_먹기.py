n, m = map(int, input().split())

field = list()

for _ in range(n):
    field.append(list(map(int, input().split))[:m])


def dfs(graph, start, visited):
    visited[start] = True
    
    for i in graph[start]:
        if not visited[i]:
            return dfs(graph, i, visited)
