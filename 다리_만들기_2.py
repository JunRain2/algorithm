from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


# 섬의 범위를 찾아주는 bfs
def bfs(x, y, cnt):
    q = deque()
    q.append((x, y))
    graph[x][y] = cnt
    result = [(x, y)]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = cnt
                q.append((nx, ny))
                result.append((nx, ny))
    return result


cnt = 1
lands = []  # 섬을 저장
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt += 1
            lands.append(bfs(i, j, cnt))

# 직진만 가능, 거리는 2 이상
edges = []  # 섬의 다리를 저장하는 리스트
# 현재 섬과 다른 섬의 길이를 구하는 과정
for land in lands:
    for x, y in land:
        current = graph[x][y]
        for i in range(4):
            nx = x
            ny = y
            cnt = -1
            while True:
                nx += dx[i]
                ny += dy[i]
                cnt += 1
                if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == current:
                    break
                if graph[nx][ny] != 0 and cnt > 1:
                    edges.append((cnt, current, graph[nx][ny]))


edges.sort() 
parent = [i for i in range(len(lands) + 2)]


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


result = 0
for cost, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
