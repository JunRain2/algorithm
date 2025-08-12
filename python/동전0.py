n, k = map(int, input().split()) # 동전 종류, 가치의 합 

array = []
for _ in range(n):
    array.append(int(input()))

array.reverse()

result = 0
for i in array:
    if k < 0:
        break
    result += k // i
    k %= i
    

print(result)