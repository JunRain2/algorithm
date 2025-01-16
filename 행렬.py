n, m = map(int, input().split())

a_array = []
b_array = []

for _ in range(n):
    a_array.append(list(map(int, input()))[:m])

for _ in range(n):
    b_array.append(list(map(int, input()))[:m])


def reverse(x, y, array):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            array[i][j] = 1 if array[i][j] == 0 else 0


def check_array(a, b):
    for x in range(n):
        for y in range(m):
            if a[x][y] != b[x][y]:
                return False
    return True


result = 0
flag = True

for x in range(n):
    for y in range(m):
        if check_array(a_array, b_array):
            flag = False
            break
        dx = x + 2
        dy = y + 2
        if 0 <= dx < n and 0 <= dy < m:
            reverse(x, y, a_array)
            result += 1

if flag:
    print(-1)
else:
    print(result)
