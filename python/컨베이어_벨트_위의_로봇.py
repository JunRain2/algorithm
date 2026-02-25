from collections import deque

# 단방향으로 이동하는 구조 
n, k = map(int, input().split())

# 언제든지 내리는 위치에 도달할 시 내릴 수 있다.
# 로봇의 위치 -> 블록의 번호 -> 컨테이너 벨트의 위치

# 블록 내구성
blocks_durability = list(map(int, input().split()))
# 컨테이너 벨트 위의 블록의 위치
block_position = deque(list(range(2*n)))
# 블록 위 로봇의 위치 -> 올라온 순서대로 이동하기 위해 deque
robot_position = deque() # (현재 블록 위치)


def is_end(arr):
    return arr.count(0) >= k

answer = 0
while not is_end(blocks_durability):
    # 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
    #   맨 뒤의 요소를 맨 앞으로 이동
    block_position.appendleft(block_position.pop())
    
    # 현재 n 위치의 블록에 로봇이 존재한다면 로봇을 내림
    if(block_position[n-1] in robot_position):
        robot_position.remove(block_position[n-1])
    
    # 로봇을 한 칸씩 이동시킴
    tmp = deque()
    for _ in range(len(robot_position)):
        pos = robot_position.popleft()
        next = (pos + 1) % (2 * n)
        
        # 로봇이 이미 존재하거나 내구성이 0인 경우 이동 X
        if next in robot_position or blocks_durability[next] <= 0:
            robot_position.append(pos)
        # 이동 가능한 경우
        else:
            # 내구성을 1 감소
            blocks_durability[next] -= 1
            # 다음 장소로 이동
            robot_position.append(next)
    
    # 현재 n 위치의 블록에 로봇이 존재한다면 로봇을 내림
    if(block_position[n-1] in robot_position):
        robot_position.remove(block_position[n-1])
        
    # 로봇을 올림
    zero_pos_block = block_position[0] # 현재 0위치에 있는 블록 
    # 내구성이 0보다 크면서 로봇이 없어야 함
    if blocks_durability[zero_pos_block] > 0 and zero_pos_block not in robot_position:
        # 내구성을 1감소
        blocks_durability[zero_pos_block] -= 1
        # 로봇을 올림
        robot_position.append(zero_pos_block)
    
    answer += 1
    
print(answer)