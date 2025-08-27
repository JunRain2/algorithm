from collections import deque


def solution(places):
    answer = []

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    def bfs(x, y, place):
        visited = [[False] * 5 for _ in range(5)]
        q = deque([(x, y, 0)])  # (x, y, 거리)
        visited[x][y] = True

        while q:
            tx, ty, dist = q.popleft()

            for i in range(4):
                nx, ny = tx + dx[i], ty + dy[i]

                if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                    if place[nx][ny] == "X":  # 파티션은 통과 불가
                        continue

                    if place[nx][ny] == "P" and dist + 1 <= 2:  # 거리두기 위반
                        return False

                    if dist + 1 < 2:  # 거리가 2 미만이면 계속 탐색
                        visited[nx][ny] = True
                        q.append((nx, ny, dist + 1))

        return True

    for place in places:
        place = [list(p) for p in place]
        flag = True

        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    if not bfs(i, j, place):
                        flag = False
                        break
            if not flag:
                break

        answer.append(1 if flag else 0)

    return answer
