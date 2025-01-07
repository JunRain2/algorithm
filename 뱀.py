n = int(input())

data = [[-1] * n for _ in range(n)]
data[0][0] = 0  # 첫 위치에서 시작
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 동남서북

k = int(input())

for _ in range(k):
    x, y = map(int, input().split())
    data[y][x] = 4

l = int(input())

result = 0
d = 0

start = (0, 0)
end = (0, 0)
for _ in range(l):
    step, direct = input().split()
    for _ in range(int(step)):
        forward_x, forward_y = directions[d]
        x = forward_x + start[0]
        y = forward_y + start[1]

        if (
            x >= n or y >= n or x < 0 or y < 0 or (data[y][x] >= 0 and data[y][x] < 4)
        ):  # 전진하지 못할 때
            break
        if data[y][x] == 4:  # 사과 였을 때
            data[y][x] = d
        else:  # 사과가 아닐 때
            data[y][x] = d
            tail_x, tail_y = end
            tail_d = data[tail_y][tail_x]
            data[tail_y][tail_x] = -1
            end = (tail_x + directions[tail_d][0], tail_y + directions[tail_d][1])
        result += 1
        start = (x, y)
    if direct == "L":
        d = (d - 1) % 4
    elif direct == "D":
        d = (d + 1) % 4

print(result)
