from collections import deque

# 매 분마다 고슴도치는 인접한 4칸으로 이동
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
# 물이 있는 칸과 인접해있는 비어있는 칸은 물이 차게 된다.
# 물과 고슴도치는 돌을 통과할 수 없다.
# 고슴도치는 물로 차있는 구역으로 이동할 수 없고, 물도 비버의 소굴로 이동할 수 없다.
# 고슴도치가 안전하게 비버의 굴로 이동하기 위해 필요한 최소 시간을 구하는 프로그램

r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]

# 고슴도치 이동 먼저, 다음 물

turn = 0
q = deque()
visited = [[-1] * c for _ in range(r)]
waters = set()


for x in range(r):
    for y in range(c):
        if graph[x][y] == 'S':
            q.append((x, y, 1))
            visited[x][y] = 0
        elif graph[x][y] == '*':
            waters.add((x, y))

# 물이 늘어남
def expand(waters):
    result = set()
    for x, y in waters:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == ".":
                result.add((nx, ny))
    waters = waters.union(result)
    return waters
    
while q:
    x, y, current = q.popleft()
    # 턴이 지났을 때, 물을 확장 -> BFS이기 때문에 트리로 따졌을 때, 같은 레벨을 다 순회한 후 다음 레벨로 진행
    if turn != current:
        waters = expand(waters)
        turn += 1
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and (nx, ny) not in waters and visited[nx][ny] == -1:
            # 도착지에 도착한 경우
            if graph[nx][ny] == 'D':
                print(visited[x][y] + 1)
                exit()
            # 아무것도 없는 경우
            if graph[nx][ny] == '.':
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny, turn + 1))

print("KAKTUS")
    