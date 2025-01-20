n = int(input())  # n * n개의 사탕

array = []
for _ in range(n):
    array.append(list(input()))


# 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y
def max_length(array):
    result = 0
    for i in range(n):
        for j in range(n):
            x_cnt = 1
            for x in range(i + 1, n):
                if array[i][j] == array[x][j]:
                    x_cnt += 1
            y_cnt = 1
            for y in range(j + 1, n):
                if array[i][j] == array[i][y]:
                    y_cnt += 1
            result = max(result, x_cnt, y_cnt)
    return result

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0
for x in range(n):
    for y in range(n):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0 <= ny < n:
                array[x][y], array[nx][ny] = array[nx][ny], array[x][y]
                result = max(result, max_length(array))
                if result == n:
                    break
                array[x][y], array[nx][ny] = array[nx][ny], array[x][y]
                
print(result)