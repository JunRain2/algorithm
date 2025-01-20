k = int(input())  # 1m에 자라나는 참외의 개수

array = []
max_x = 0  # 가로 최고 길이
max_y = 0  # 세로 최고 길이
min_x = 0
min_y = 0

for i in range(6):
    a, b = map(int, input().split())
    if a == 1 or a == 2:
        max_x = max(b, max_x)
    elif a == 3 or a == 4:
        max_y = max(b, max_y)
    if i == 2 and a == 4:
        min_y = b
        min_x = array[i - 1][1]
    if i == 3 and a == 2:
        min_x = b
        min_y = array[i - 1][1]
    if i == 4:
        if a == 3:  # 남
            min_y = b
            min_x = array[i - 1][1]
        if a == 1:
            min_x = b
            min_y = array[i - 1][1]
    array.append((a, b))

# 육각형을 데이터로 어떻게 표현할 것인가
# 작은 사각형을 어떻게 찾을 것인가?
max_square = max_x * max_y  # 사각형 전체 합
min_square = min_x * min_y

result = k * (max_square - min_square)
print(result)
