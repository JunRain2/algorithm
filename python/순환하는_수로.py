# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

n = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(n):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

parent = list(range(n + 1))

def dfs(v, prev, path):
	parent[v] = prev
	path.add(v)

	for next in graph[v]:
		if next == prev:
			continue

		if parent[next] != next: # 이미 방문 -> Circle일 가능성 존재
			if next in path: # 지나온 경로에 next 존재 -> Circle 확정 !!!
				current = v
				circle = []
				while current != next:
					circle.append(current)
					current = parent[current]

				circle.append(next) # next를 맨 마지막에 추가
				return circle

		circle = dfs(next, v, path)
		if circle:
			return circle

	return None


circle = None
for i in range(n):
	if parent[i] == i:
		circle = dfs(i, 0, set()) # set()은 매 그래프마다 초기화되기 때문에 remove를 따로 할 필요 없음
		if circle:
			break

print(len(circle))
print(*sorted(circle))