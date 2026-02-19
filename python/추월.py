from copy import deepcopy

n = int(input())

# 들어간 순서대로 나와야 함

# 현재 차 이전에 들어간 차량들
cars = dict()
tmp = set()
for _ in range(n):
    s = input()
    cars[s] = deepcopy(tmp)
    
    tmp.add(s)

    
tmp = set()
result = 0
# 순서대로 나오는지 검사해야함, 그니깐 필요조건(이전에 지나간 차)가 만족하는지 확인
for i in range(n):
    s = input()

    # 나오는 차량 중에 이전 차량 순서에 포함이 안되는 차량이 한 대라도 있으면 추월
    if not (cars[s] <= tmp):
        result += 1
        
    tmp.add(s)

print(result)