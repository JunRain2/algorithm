# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

path = []

def dfs(graph, visited, v, prev):
	visited[v] = True

	for next in graph[v]:
		if next == prev:
			continue

		if not visited[next]:
			path.append(next)
			
			if dfs(graph, visited, next, v):
				return True
			
			path.pop()
		else: # Circle 발생 가능성 존재
			if next in path: # Circle 발생
				path.append(next)
				return True

	return False

visited = [False for _ in range(n + 1)]

for i in range(1, n + 1):
	if not visited[i]:
		path.append(i)
		if dfs(graph, visited, i, -1):
			break
		path.pop()

for i in range(len(path)):
	if path[i] == path[-1]:
		path = path[i:-1]
		break

print(len(path))
print(*sorted(path))
