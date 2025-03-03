n = int(input())
data = [tuple(map(int, input().split())) for _ in range(n)]
# 거리, 원래 있던 연료의 양
l, p = map(int, input().split())
data = [(0, p)] + data + [(l, 0)]

"""
현재 어떤 정보를 가지고 최적의 선택을 할 것인가?
1. 현재 주유를 해야하는가?
2. 해야한다면 왜 해야하는가?
- 현재 남은 주유를 통해서 다음 거리를 갈 수 없기 때문
- 현재 주유를 안하면 완주를 할 수 없기 때문 [v]
"""
total = sum(x[1] for x in data) # 주유할 수 있는 전체 연료
current = 0 # 현재 연료
answer = -1
for i in range(n + 1):  # 다음 목적지, 다음 목적지의 연료
    now, f = data[i]  # 현재 위치
    next = data[i + 1][0]  # 다음 위치
    
    gap = next - now
    
    if current - gap < 0 and total + current - f < l: 
        answer = - 1
        break
    # 다음으로 갈 수 없거나 완주가 불가능한 경우
    elif current - gap < 0 or total + current - f < l: 
        answer += 1
        current += f
    
    current -= gap
    l -= gap
    total -= f

print(answer)