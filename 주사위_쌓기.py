import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]


def dfs(k, v):
    if k >= n:
        return 0

    idx = data[k].index(v)
    if idx == 0:
        return dfs(k + 1, data[k][5]) + max(
            data[k][1], data[k][2], data[k][3], data[k][4]
        )
    elif idx == 1:
        return dfs(k + 1, data[k][3]) + max(
            data[k][0], data[k][2], data[k][5], data[k][4]
        )
    elif idx == 2:
        return dfs(k + 1, data[k][4]) + max(
            data[k][1], data[k][0], data[k][3], data[k][5]
        )
    elif idx == 3:
        return dfs(k + 1, data[k][1]) + max(
            data[k][0], data[k][2], data[k][4], data[k][5]
        )
    elif idx == 4:
        return dfs(k + 1, data[k][2]) + max(
            data[k][1], data[k][5], data[k][3], data[k][0]
        )
    else:
        return dfs(k + 1, data[k][0]) + max(
            data[k][1], data[k][2], data[k][3], data[k][4]
        )


result = 0
for i in range(1, 7):
    result = max(result, dfs(0, i))

print(result)
