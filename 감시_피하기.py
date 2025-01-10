from itertools import combinations
import copy

n = int(input())
array = []
tmp = []
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for i in range(n):
    array.append(input().split())
    for j in range(n):
        if array[i][j] == "X":
            tmp.append((i, j))


def dfs(start, array):
    x, y = start
    array[x][y] = "T"
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < 0 and array[nx][ny] == "X":
            if array[nx][ny] == "O":
                return True
            if array[nx][ny] == "S":
                return False
            return dfs((nx, ny), array)


result = False
for i in combinations(tmp, 3):
    if result:
        break
    array_tmp = copy.deepcopy(array)
    for j in i:
        a, b = j
        array_tmp[a][b] = "O"

    for x in range(n):
        for y in range(n):
            if array_tmp[x][y] == "T":
                result = dfs((x, y), array_tmp)

output = "YES" if result else "NO"
print(output)
