from collections import deque

n, m = map(int, input().split())  # m개의 흩어진 열쇠
nodes = [] # 키와 출발지를 노드로 설정
graph = []
cnt = 2
for i in range(n):

    data = list(input())
    for j in range(n):
        if data[j] == "S" or data[j] == "K":
            data[j] = cnt
            nodes.append((i, j))
            cnt += 1
        else:
            data[j] = int(data[j])
    graph.append(data)


# 로봇이 움직이는 횟수의 합을 최소로 하는 프로그램
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

edges = []

# 노드들을 최솟값으로 연결하는 과정
def bfs(start, edges):
    x, y = start
    visited = [[-1] * n for _ in range(n)]
    visited[x][y] = 0
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < n
                and 0 <= ny < n
                and visited[nx][ny] == -1
                and graph[nx][ny] != 1
            ):
                visited[nx][ny] = visited[x][y] + 1
                if graph[nx][ny] > 1:
                    edges.append(
                        (visited[nx][ny], graph[start[0]][start[1]], graph[nx][ny])
                    )
                q.append((nx, ny))

for node in nodes:
    bfs(node, edges)


edges.sort()
parent = list(range(m + 3))


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
        result += cost
        union_parent(parent, a, b)
        
# 모든 키를 찾았는지 확인       
for i in range(2, m + 2):
    if find_parent(parent, i) != find_parent(parent, i + 1):
        print(-1)
        exit()
        
print(result)