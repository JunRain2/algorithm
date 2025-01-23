n = int(input())
array = []
negative_array = []
result = 0
for i in range(n):
    data = int(input())
    if 0 > data:
        negative_array.append(data)
    else:
        if data == 1:
            result += 1
        else:
            array.append(data)

array.sort()  # 0을 포함한 양수
negative_array.sort()  # 음수


if negative_array:
    if len(negative_array) % 2 == 0:  # 짝수
        while negative_array:
            a1, a2 = negative_array.pop(), negative_array.pop()
            result += a1 * a2
    elif len(negative_array) % 2 == 1:  # 홀수
        if array and array[0] == 0:
            array.pop(0)
            negative_array.pop(-1)
        else:
            result += negative_array.pop(-1)
        while negative_array:
            a1, a2 = negative_array.pop(), negative_array.pop()
            result += a1 * a2

if array:
    while array and array[0] == 0:
        array.pop(0)
    if len(array) % 2 == 0:
        while array:
            a1, a2 = array.pop(), array.pop()
            result += a1 * a2
    elif len(array) % 2 == 1:
        result += array.pop(0)
        while array:
            a1, a2 = array.pop(), array.pop()
            result += a1 * a2


print(result)
