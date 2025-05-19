import sys
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
escape = [[False] * m for _ in range(n)]  # 탈출 가능한 칸

# 방향 매핑
directions = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

def dfs(y, x):
    if visited[y][x]:
        return escape[y][x]

    visited[y][x] = True
    dy, dx = directions[graph[y][x]]
    ny, nx = y + dy, x + dx

    if ny < 0 or ny >= n or nx < 0 or nx >= m:
        escape[y][x] = True  # 밖으로 나감 → 탈출 가능
    else:
        escape[y][x] = dfs(ny, nx)  # 다음 칸 결과 재귀

    return escape[y][x]

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)