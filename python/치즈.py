from collections import deque

# 2변 이상 -> 한 시간
# 치즈 내부는 외부 공간에 접촉하지 않은 것으로 가정
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0 ,1]

# 공기 유입에 대해 생각 -> 공기 유입만 없었더라면 주위 0인 경우
# 가장 자리는 X (0, 0) 부터 시작
def bfs(visited, graph, count):
    q = deque([(0, 0)])
    visited[0][0] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    count[nx][ny] += 1
                elif not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))


def check_cheese(graph):
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                return True
    return False

def melting_cheese(graph, count):
    for i in range(n):
        for j in range(m):
            if count[i][j] >= 2:
                graph[i][j] = 0

answer = 0
while check_cheese(graph):
    visited = [[False] * m for _ in range(n)]
    count = [[0] * m for _ in range(n)]
    bfs(visited, graph, count)
    melting_cheese(graph, count)
    answer += 1
        
print(answer)