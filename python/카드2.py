from collections import deque

n = int(input())
if n == 1:
    print(1)
    exit()

q = deque(range(1, n + 1))

# 카드가 마지막 한 장일 때를 포착해야함 -> 카드를 버렸을 때 1장인 경우
while True:
    q.popleft()
    
    if len(q) == 1:
        print(q[0])
        exit()
        
    q.append(q.popleft())