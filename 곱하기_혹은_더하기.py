data = list(map(int, input()))

result = data[0]

for i in data[1:]:
    result = max(result * i, result + i)

print(result)
