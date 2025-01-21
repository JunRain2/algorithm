from collections import deque

dx = [-1, 0, 1, 0]  # 상, 좌, 하, 우
dy = [0, -1, 0, 1]

def bfs_normal(x, y, color):
    """정상 시야 BFS"""
    queue = deque()
    queue.append((x, y))
    visited_normal[x][y] = True

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            # 범위 내에 있고 아직 방문 안 했으며, 같은 색이면 방문
            if 0 <= nx < n and 0 <= ny < n:
                if not visited_normal[nx][ny] and array[nx][ny] == color:
                    visited_normal[nx][ny] = True
                    queue.append((nx, ny))

def bfs_colorblind(x, y, color):
    """적록색약 BFS ('R'과 'G'를 같은 색으로 취급)"""
    queue = deque()
    queue.append((x, y))
    visited_cb[x][y] = True

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited_cb[nx][ny]:
                # R/G 그룹이면 R/G 모두 같은 영역으로 본다
                if color in ('R', 'G'):
                    if array[nx][ny] in ('R', 'G'):
                        visited_cb[nx][ny] = True
                        queue.append((nx, ny))
                # B 그룹이면 B만 같은 영역
                else:  # color == 'B'
                    if array[nx][ny] == 'B':
                        visited_cb[nx][ny] = True
                        queue.append((nx, ny))

n = int(input().strip())
array = [list(input().strip()) for _ in range(n)]

visited_normal = [[False]*n for _ in range(n)]  # 정상 시야 방문 체크
visited_cb = [[False]*n for _ in range(n)]      # 적록색약 시야 방문 체크

normal_count, cb_count = 0, 0

# 1. 정상 시야로 구역 수 계산
for i in range(n):
    for j in range(n):
        if not visited_normal[i][j]:
            normal_count += 1
            bfs_normal(i, j, array[i][j])

# 2. 적록색약 시야로 구역 수 계산
for i in range(n):
    for j in range(n):
        if not visited_cb[i][j]:
            cb_count += 1
            bfs_colorblind(i, j, array[i][j])

print(normal_count, cb_count)
