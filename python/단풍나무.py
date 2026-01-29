# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 반복문 종료 조건
def check_end():
	# 전체 합이 0 -> 그래프 전부가 0
	return sum(map(sum, graph)) != 0

# 주위 0인 값이 얼마나 있는지 
def cnt_d(x, y):
	dx = [-1, 0, 1, 0]
	dy = [0, 1, 0, -1]

	c = 0
	for i in range(4):
		nx, ny = x + dx[i], y + dy[i]
		c += (0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0)

	return c
	
result = 0
while check_end():
	current = [[0] * n for _ in range(n)]
	for x in range(n):
		for y in range(n):
			if graph[x][y] != 0:
				current[x][y] = max(0, graph[x][y] - cnt_d(x, y))

	graph = current
	result += 1

print(result)

