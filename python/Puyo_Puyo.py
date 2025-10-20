from collections import deque

# 바닥이나 다른 뿌요가 나올 때까지 아래로 떨어짐
# 같은 색 뿌요가 4개 이상 상하좌우로 연결돼 있으면 한꺼번에 사라진다.
# 뿌요들이 없어지고 나서 위에 다른 뿌요가 있다면, 중력에 영향을 받아 아래로 떨어짐
# 아래로 떨어지고 나서 다시 같은 색의 뿌요들이 있다면 차례대로 아래로 떨어짐
# 터질 수 있는 뿌요가 여러 그룹이 있다면 동시에 터져야 하고 여러 그룹이 터지더라도 한번의 연쇄가 추가

n, m = 12, 6

graph = [list(input()) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

flag = True


# 같은 색의 포뇨의 좌표를 반환
def bfs(graph, start):
    x, y = start
    visited = set()

    color = graph[x][y]
    q = deque([(x, y)])
    visited.add((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (
                0 <= nx < n
                and 0 <= ny < m
                and graph[nx][ny] == color
                and (nx, ny) not in visited
            ):
                visited.add((nx, ny))
                q.append((nx, ny))

    return visited


# 아래서부터 한칸씩 땡김
def drop():
    global graph

    for x in range(n - 2, -1, -1):
        for y in range(m):
            if graph[x][y] != ".":
                nx = x
                for i in range(x + 1, n):
                    if graph[i][y] == ".":
                        nx = i
                graph[nx][y], graph[x][y] = graph[x][y], graph[nx][y]


result = 0
while True:
    visited = set()
    flag = False

    for x in range(n):
        for y in range(m):
            if graph[x][y] != ".":
                v = bfs(graph, (x, y))
                # 길이가 4 이상인 경우 연쇄가 시작됨
                if len(v) >= 4:
                    flag = True
                    # 터진 포뇨 때문에 빈칸으로 표시
                    for nx, ny in v:
                        graph[nx][ny] = "."

                visited = visited.union(v)

    if not flag:
        break
    # 하나의 턴에서 연쇄가 끝난 후, 아래로 내림
    drop()
    result += 1

print(result)
