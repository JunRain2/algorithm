import heapq


def dfs(cnt, start, end):
    x, y = start
    if start == end or graph[x][y] == shark_size:
        return cnt
    if x < 0 or x >= n or y < 0 or y >= n or graph[x][y] != 0:
        return int(1e9)
    a = dfs(cnt + 1, (x + 1, y), end)
    b = dfs(cnt + 1, (x - 1, y), end)
    c = dfs(cnt + 1, (x, y + 1), end)
    d = dfs(cnt + 1, (x, y - 1), end)

    return min(a, b, c, d)


n = int(input())
graph = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

q = []
shark_x = shark_y = -1
for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(n):
        if data[j] == 9:
            shark_x, shark_y = i, j
        elif data[j] != 0:
            heapq.heappush(q, (data[j], i, j))


shark_size = 2
shark_level = 4
result = 0
while q:
    fish_size, fish_x, fish_y = heapq.heappop(q)
    if shark_size < fish_size:
        break

    # 이동 최솟값을 구하는 함수
    result += dfs(0, (shark_x, shark_y), (fish_x, fish_y))
    if result >= int(1e9):
        result -= int(1e9)
        break

    shark_level -= fish_size
    if shark_level <= 0:
        shark_size += 1
        shark_level += shark_size**2


print(result)
