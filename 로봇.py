# 로봇을 원하는 위치로 이동시키고, 원하는 방향을 바라보도록 하는 방법
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 동, 서, 남, 북
directions = [0, 1, 3, 2, 0]
# 시작점, 방향
sx, sy, sd = map(int, input().split())
sx, sy, sd = sx - 1, sy - 1, directions[sd]
# 도착점, 방향
ex, ey, ed = map(int, input().split())
ex, ey, ed = ex - 1, ey - 1, directions[ed]


# 북(0), 동(1), 남(2), 서(3)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = set()

# 현재 위치, 방향, 현재 횟수
q = deque([(sx, sy, sd, 0)])
visited.add((sx, sy, sd))

while q:
    x, y, d, cnt = q.popleft()
    if (x, y, d) == (ex, ey, ed):
        print(cnt)
        exit()

    # k(1 ~ 3)만큼 움직이는 경우
    nx, ny = x, y
    for _ in range(3):
        nx += dx[d]
        ny += dy[d]

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            if (nx, ny, d) not in visited:
                q.append((nx, ny, d, cnt + 1))
                visited.add((nx, ny, d))
        else:
            break

    # 왼쪽으로 회전하는 경우
    ld = (d - 1) % 4
    if (x, y, ld) not in visited:
        q.append((x, y, ld, cnt + 1))
        visited.add((x, y, ld))

    # 오른쪽으로 회전하는 경우
    rd = (d + 1) % 4
    if (x, y, rd) not in visited:
        q.append((x, y, rd, cnt + 1))
        visited.add((x, y, rd))
