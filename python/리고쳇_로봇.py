from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def solution(board):
    answer = -1
    board = [list(row) for row in board]

    row = len(board)
    column = len(board[0])
    visited = [[-1] * column for _ in range(row)]

    for i in range(row):
        for j in range(column):
            if board[i][j] == "R":
                q = deque([(i, j)])
                visited[i][j] = 0
                while q:
                    x, y = q.popleft()
                    if board[x][y] == "G":
                        return visited[x][y]

                    for i in range(4):
                        nx, ny = x, y
                        while True:
                            tx, ty = nx + dx[i], ny + dy[i]
                            if (
                                0 > tx
                                or tx >= row
                                or ty < 0
                                or ty >= column
                                or board[tx][ty] == "D"
                            ):
                                if visited[nx][ny] == -1:
                                    visited[nx][ny] = visited[x][y] + 1
                                    q.append((nx, ny))
                                break

                            nx, ny = tx, ty

    return -1
