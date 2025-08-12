from collections import deque

# 문자 하나 -> 지게차로
# 문자 두 개의 -> 크레인

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def move_car(storage, request, n, m):
    visited = [[False] * m for _ in range(n)]
    counter = 0
    q = deque([(0, 0)])
    visited[0][0] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and storage[nx][ny] == "0":
                    q.append((nx, ny))
                    visited[nx][ny] = True

                elif storage[nx][ny] == request:
                    storage[nx][ny] = "0"
                    visited[nx][ny] = True
                    counter += 1
    print(counter)
    return counter


def move_crain(storage, request, n, m):
    counter = 0
    for i in range(n):
        for j in range(m):
            if storage[i][j] == request:
                counter += 1
                storage[i][j] = "0"
    print(counter)
    return counter


def solution(storage, requests):
    n, m = len(storage) + 2, len(storage[0]) + 2

    answer = len(storage) * len(storage[0])

    graph = []

    graph.append(["0"] * m)
    for s in storage:
        graph.append(["0"] + list(s) + ["0"])
    graph.append(["0"] * m)

    for request in requests:
        if len(request) == 2:
            answer -= move_crain(graph, request[0], n, m)
        else:
            answer -= move_car(graph, request, n, m)

    return answer
