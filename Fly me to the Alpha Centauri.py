import sys

sys.setrecursionlimit(10**5)

for tc in range(int(input())):
    x, y = map(int, input().split())
    n = y - x

    dx = [-1, 0, 1]

    def dfs(v, k, cnt):
        if v == n and k == 1:
            return cnt
        if k <= 0 or v > n + 1 or v < 1:
            return int(2**31)

        tmp = []
        for i in range(3):
            tmp.append(dfs(v + (k + dx[i]), k + dx[i], cnt + 1))
        return min(tmp)

    print(dfs(1, 1, 1))
