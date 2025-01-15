g = int(input())
p = int(input())

airport = [0] * (g + 1)

data = []
for _ in range(p):
    data.append(int(input()))

result = 0
for i in data:
    result += 1
    airport[i] += 1
    tmp_value = 0
    for j in range(1, i + 1):
        tmp_value += airport[j]
    if tmp_value > i:
        result -= 1
        break
    
print(result)