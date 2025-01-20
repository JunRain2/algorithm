n = int(input())  # n * n개의 사탕

array = []
for _ in range(n):
    array.append(list(input()))


# 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y
def max_length(array):
    max_cnt = 1
    
    # 가로 방향 체크
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if array[i][j] == array[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)
    
    # 세로 방향 체크
    for j in range(n):
        cnt = 1
        for i in range(1, n):
            if array[i][j] == array[i-1][j]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)
    
    return max_cnt


dx = [1, 0]
dy = [0, 1]

result = 0
for x in range(n):
    for y in range(n):
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and array[x][y] != array[nx][ny]:
                array[x][y], array[nx][ny] = array[nx][ny], array[x][y]
                result = max(result, max_length(array))
                if result == n:
                    break
                array[x][y], array[nx][ny] = array[nx][ny], array[x][y]

print(result)
