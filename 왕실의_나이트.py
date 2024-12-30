a = input()

x = int(ord(a[0])) - 97
y = int(a[1]) - 1

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

cnt = 0
for i in range(8):
    tmp_x = x + dx[i]
    tmp_y = y + dy[i]
    
    if tmp_x < 0 or tmp_x >= 8 or tmp_y < 0 or tmp_y >= 8:
        continue
    
    cnt += 1

print(cnt)