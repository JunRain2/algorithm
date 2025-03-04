import sys
input = sys.stdin.readline

def dfs(x, y):
    if visited[x][y]:
        if visited[x][y] == 1:  # 현재 탐색 중인 경로에서 사이클 발견
            return 1
        return 0  # 이미 완료된 경로
    
    visited[x][y] = 1  # 현재 탐색 중 표시
    nx, ny = x + direction[graph[x][y]][0], y + direction[graph[x][y]][1]
    result = dfs(nx, ny)
    visited[x][y] = 2  # 탐색 완료 표시
    return result

# 입력 받기
N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]

# 방향 정의
direction = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

# 방문 배열 초기화
visited = [[0] * M for _ in range(N)]

safe_zones = 0

# 모든 칸에 대해 DFS 수행
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            safe_zones += dfs(i, j)

print(safe_zones)
