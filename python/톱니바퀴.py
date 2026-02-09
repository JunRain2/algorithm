# 8개의톱니를 갖고 있는 톱니바퀴 4개

# 서로 맞닿은 극에 따라 톱니바퀴를 회전시킬 수 있고 아닐 수 있다.
# 서로 맞닿은 극이 다르면 A의 회전 방향과 반대 방향으로 
# 극이 같으면 정지
# 옆에 것이 움직였으면 
from copy import deepcopy

gears = []

for _ in range(4):
    gears.append(list(map(int, list(input()))))
    
"""
1번 기어는 2번 기어
2번 기어는 1번 기어, 3번 기어
3번 기어는 2번 기어, 3번 기어
4번 기어는 3번 기어
"""
def reverse(dir):
    if dir == -1:
        return 1
    else:
        return -1
    
def turn(gear, dir):
    result = [0] * 8
    if dir == 1:
        for i in range(8):
            result[(i + 1) % 8] = gear[i]
    else:
        for i in range(8):
            result[(i - 1) % 8] = gear[i]
            
    return result

for _ in range(int(input())):
    # n을 기준으로 좌우로 전파되어야 함
    # 오른쪽 index = 2, 왼쪽 index = 6
    n, dir = map(int, input().split())
    n = n - 1
    
    left = n - 1 # 초깃값으로 3이 올 수 없음
    right = n + 1 # 초깃값으로 0이 올 수 없음
    
    result = deepcopy(gears)
    
    # 왼쪽으로 전파
    current_dir = dir
    while left >= 0:
        prev = left + 1
        
        # 극이 같으면 전파를 멈춤
        if gears[prev][6] == gears[left][2]:
            break
        
        # 극이 다르면 반대 방향으로 움직임 
        current_dir = 1 if current_dir == -1 else -1
        result[left] = turn(gears[left], current_dir)
        
        left -= 1
        
    # 오른쪽으로 전파
    current_dir = dir
    while right < 4: # right가 처음에 0이 올 수 없음
        prev = right - 1
        
        if gears[prev][2] == gears[right][6]:
            break
        
        current_dir = 1 if current_dir == -1 else -1
        result[right] = turn(gears[right], current_dir)
        right += 1
        
    # 본인 회전
    result[n] = turn(gears[n], dir)
    gears = result

score = 0
for i in range(4):
    if gears[i][0] == 1:
        score += 2**i

print(score)