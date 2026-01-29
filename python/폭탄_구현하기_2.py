# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n, k = map(int, input().split())

data = [list(input().split()) for _ in range(n)]
graph = [[0] * (n + 1) for _ in range(n + 1)]

def boom(y, x):
	dx = [-1, 0, 1, 0]
	dy = [0, 1, 0, -1]

	graph[y][x] += cal_score(data[y - 1][x - 1])
	for i in range(4):
		ny, nx = y + dy[i], x + dx[i]
		
		if 0 < ny <= n and 0 < nx <= n:
			graph[ny][nx] += cal_score(data[ny - 1][nx - 1])


def cal_score(state):
	if state == '#':
		return -2
	if state == '@':
		return 2
	return 1


for _ in range(k):
	y, x = map(int, input().split())

	boom(y, x)

print(max(map(max, graph)))
