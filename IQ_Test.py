n = int(input())
array = list(map(int, input().split()))

if len(array) == 1 or (len(array) == 2 and array[0] != array[1]):
    print("A")
    exit()

data = set()
for i in range(1, n):
    if array[i - 1] == 0: # 0, 1, 2의 경우
        a, b = 1, array[i] 
    else:
        a, b = divmod(array[i], array[i - 1])
        if a == 0: # 3,2,1의 경우
            a, b = 1, -b
    data.add((a, b))


result = set()
# 검증하는 과정
for a, b in data:
    flag = True
    prev = array[0]
    for i in range(1, n):
        if array[i] == (a * prev + b):
            prev = array[i]
        else:
            flag = False
            break
    if flag:
        result.add(a * prev + b)
        
if len(result) >= 2:
    print('A')
elif not result:
    print('B')
else:
    print(list(result)[0])
