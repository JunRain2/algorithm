from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def solution(land):
    n = len(land)
    m = len(land[0])

    # 석유의 크기
    def bfs(x, y, visited, answer):
        q = deque([(x, y)])
        visited[x][y] = True
        start_y = end_y = y

        cnt = 1
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (
                    0 <= nx < n
                    and 0 <= ny < m
                    and not visited[nx][ny]
                    and land[nx][ny] == 1
                ):
                    cnt += 1
                    visited[nx][ny] = True
                    start_y = min(start_y, ny)
                    end_y = max(end_y, ny)
                    q.append((nx, ny))

        for i in range(start_y, end_y + 1):
            answer[i] += cnt

    answer = [0] * m
    vist = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not vist[i][j] and land[i][j] == 1:
                bfs(i, j, vist, answer)

    print(answer)

    return max(answer)
