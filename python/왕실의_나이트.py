input_data = input()

row = int(input_data[1])
column = int(ord(input_data[0]) - int(ord('a'))) + 1 # 아스키 코드를 못외웠으면 그냥 이렇게 사용

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)