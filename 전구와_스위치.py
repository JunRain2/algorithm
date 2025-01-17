n = int(input())

data = list(map(int, input()))  # 바꿀 배열
array = list(map(int, input()))  # 같게 만들어야 하는 배열


def switch(data, i):
    if i == 0 or i == n - 2:
        for j in range(i, i + 2):
            data[j] = 0 if data[j] == 1 else 1
    else:
        for j in range(i, i + 3):
            data[j] = 0 if data[j] == 1 else 1


flag = False
result = 0
for i in range(n):
    if data[i] != array[i]:
        result += 1
        switch(data, 1)

    if data == array:
        flag = True
        break

if flag:
    print(result)
else:
    print(-1)
