import sys
sys.setrecursionlimit(100000) # 재귀의 수를 늘려줌

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
max_height = max(map(max, array))
min_height = min(map(min, array))

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def dfs(x, y, visited, min_height):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and array[nx][ny] > min_height:
            dfs(nx, ny, visited, min_height)


result = 1
for i in range(min_height, max_height + 1):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for x in range(n):
        for y in range(n):
            if not visited[x][y] and array[x][y] > i:
                cnt += 1
                dfs(x, y, visited, i)

    result = max(result, cnt)

print(result)
