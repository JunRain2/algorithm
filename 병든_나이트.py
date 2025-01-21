from collections import deque

dx = [-2, -1, 1, 2]
dy = [1, 2, 2, 1]

n, m = map(int, input().split())  # 세로 길이, 가로 길이

flag = [False] * 4

q = deque()
q.append((n, 0))
result = 0
while q:
    x, y = q.popleft()
    result += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            q.append((nx, ny))
            flag[i] = True
            
if result > 4:
    result_flag = True
    for f in flag:
        if not f:
            result_flag = False

if not result_flag:
    print(4)
else:
    print(result)