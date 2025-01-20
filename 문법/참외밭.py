k = int(input())
directions = []
lengths = []

for i in range(6):
    direction, length = map(int, input().split())
    directions.append(direction)
    lengths.append(length)

# 방향과 길이를 두 번 이어붙여서 패턴을 찾기 쉽게 함
directions = directions + directions
lengths = lengths + lengths

max_area = 0
min_area = 0

# 전체 육각형에서 가장 긴 가로, 세로 찾기
width = max([lengths[i] for i in range(6) if directions[i] in [1, 2]])
height = max([lengths[i] for i in range(6) if directions[i] in [3, 4]])
max_area = width * height

# 빈 사각형 찾기
for i in range(6):
    # 연속된 네 변에서 첫 번째와 세 번째, 두 번째와 네 번째가 각각 평행할 때
    if directions[i] == directions[i+2] and directions[i+1] == directions[i+3]:
        min_area = lengths[i+1] * lengths[i+2]
        break

result = (max_area - min_area) * k
print(result)
