from collections import deque
import heapq

n, t, w = map(int, input().split())

# x번 손님의 id, 업무를 처리하는 데 필요한 시간
first = deque()
for _ in range(n):
    px, tx = map(int, input().split())
    first.append((px, tx))
    
m = int(input())

second = []
for _ in range(m):
    # x번 손님의 id, 필요한 시간, 영업 시작 c초 후
    px, tx, cx = map(int, input().split())
    
    heapq.heappush(second, (cx, px, tx))

# second는 결국 c초 후에 들어갈 것

answer = []
time_left = w
while first and time_left > 0:
    ci, ct = first.popleft()
    # 사용자에게 남은 시간
    rt = max(ct - t, 0)
    
    # loop 만큼 돌리는데, loop가 w보다 크다면 w만큼 loop를 돌림
    # 몇 초 동안 사용자를 처리했는지 알 필요가 존재 
    loop = min(time_left, ct - rt)
    
    answer.extend([ci] * loop)
    # w를 얼마나 잡아먹었는가.
    time_left -= loop
    if time_left <= 0: # 시간을 다 썼으므로 종료
        break
    
    # 흘러간 시간이랑 seconds에 있는 사람이 들어오는 시간 비교
    while second and second[0][0] <= (w - time_left):
        _, si, st = heapq.heappop(second)
        first.append((si, st))

    if rt <= 0:
        continue
    else:
        first.append((ci, rt))

for a in answer:
    print(a)