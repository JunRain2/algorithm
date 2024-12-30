n, m = map(int, input().split())

x, y, direction = map(int, input().split())

field = list()
for _ in range(n):
    field.append(list(map(int, input().split()))[:m])
    
steps = [(0, 1), (1,0), (0, -1), (-1, 0)] # 북, 동, 남, 서
    
    
result = 0
while True:
    flag = True
    for _ in range(4):
        direction = (direction - 1) % 4 # 어째서인지 알아보기 / 문제에서 1번에 해당
        tmp_x = x + steps[direction][0]
        tmp_y = y + steps[direction][1]
        
        if field[tmp_y][tmp_x] == 0: # 문제에서 2번에 해당
            field[x][y] = 1
            result += 1
            x = tmp_x
            y = tmp_y
            flag = False
            break
    
    if flag: # 문제에서 3번에 해당
        tmp_direction = (direction + 2) % 4
        if field[y + steps[tmp_direction][1]][x + steps[tmp_direction][0]] == 1:
            break
        x += steps[tmp_direction][0]
        y += steps[tmp_direction][1]
    
    
print(result)