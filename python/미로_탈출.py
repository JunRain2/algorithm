from collections import deque

n, m = map(int, input().split())

field = list()
for _ in range(n):
    field.append(list(map(int, input()))[:m])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# BFS 소스코드 구현
def bfs(x, y):
    # 큐(Queue) 구현하기 위해 deque 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인 경우 무시
            if field[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if field[nx][ny] == 1:
                field[nx][ny] = field[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return field[n - 1][m - 1]


# BFS를 수행한 결과 출력
print(bfs(0, 0))
