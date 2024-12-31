n, m = map(int, input().split())

field = list()
for _ in range(n):
    field.append(list(map(int, input()))[:m])



def dfs(x, y, cnt):
    global field
    
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return 999999999

    if x == m - 1 and y == n - 1:
        return cnt

    if field[y][x] == 0:
        return 999999999

    field[y][x] = 0
    a = dfs(x + 1, y, cnt + 1)
    b = dfs(x - 1, y, cnt + 1)
    c = dfs(x, y + 1, cnt + 1)
    d = dfs(x, y - 1, cnt + 1)

    return min(a, b, c, d)


print(dfs(0, 0, 1))
