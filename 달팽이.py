n = int(input())  # 홀수인 자연수 n
num = int(input())  # 좌표가 궁금한 수

data = [[0] * n for _ in range(n)]

start_x = start_y = 0

total = n**2
times = n
for _ in range(n**2):
    x, y = start_x, start_y
    for i in range(n): # 아래로
        if total == num:
            result = (x + 1, y + 1)
        data[x][y] = total
        total -= 1
        x += 1
    x -= 1
    y += 1
    n -= 1
    for i in range(n): # 오른쪽으로
        if total == num:
            result = (x + 1, y + 1)
        data[x][y] = total
        total -= 1
        y += 1
    y -= 1
    x -= 1
    for i in range(n): # 위로
        if total == num:
            result = (x + 1, y + 1)
        data[x][y] = total
        total -= 1
        x -= 1
    y -= 1
    x += 1
    n -= 1
    for i in range(n): # 왼쪽으로
        if total == num:
            result = (x + 1, y + 1)
        data[x][y] = total
        total -= 1
        y -= 1


    start_x += 1
    start_y += 1


for d in data:
    print(*d)
    
print(*result)