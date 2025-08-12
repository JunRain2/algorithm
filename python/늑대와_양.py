r,c = map(int, input().split())

array = [list(input()) for _ in range(r)]
# 인접하다는 것은 변을 공유한다는 의미 

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def print_array(array):
    for i in range(r):
        print(*array[i], sep='')

for i in range(r):
    for j in range(c):
        if array[i][j] == 'S':
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < r and 0 <= ny < c:
                    if array[nx][ny] == 'W':
                        print(0)
                        exit()
                    elif array[nx][ny] == '.':
                        array[nx][ny] = 'D'

print(1)
print_array(array)