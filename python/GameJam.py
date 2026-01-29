# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
gr, gc = map(int, input().split()) # 구름이
pr, pc = map(int, input().split()) # 플레이어

field = [list(input().split()) for _ in range(n)]

# 게임 시작, 점수를 반환
def play(start):
	graph = [[0] * n for _ in range(n)]
	
	current = start
	graph[current[0]][current[1]] = 1
	while True:
		point = move(current[0], current[1], graph)
		
		if point == None:
			break

		current = point
		graph[current[0]][current[1]] = 1

	return sum(map(sum, graph))


# 이동 -> 이동 후 좌표를 반환
# 이미 지나 간 곳일 경우 None을 반환
def move(x, y, graph):
	command = field[x][y]
	dis, dir = int(command[:-1]), command[-1]

	nx, ny = x, y
	for _ in range(dis):
		nx, ny = direct(dir, nx, ny)
		if graph[nx][ny] == 1:
			return None
			
		graph[nx][ny] = 1

	return nx, ny

# 명령에 맞게 한 칸씩 움직임
def direct(dir, x, y):
	if dir == "L":
		y -= 1
		if y < 0:
			y = n - 1

		return x, y

	if dir == "R":
		y += 1
		if y >= n:
			y = 0

		return x ,y

	if dir == "U":
		x -= 1
		if x < 0:
			x = n - 1
			
		return x, y

	if dir == "D":
		x += 1
		if x >= n:
			x = 0
			
		return x, y


goorm = play((gr - 1, gc - 1))
player = play((pr - 1, pc - 1))

if goorm > player:
	print("goorm", goorm)
else:
	print("player", player)