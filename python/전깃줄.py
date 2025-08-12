from bisect import bisect_left

n = int(input())
array = [tuple(map(int, input().split())) for _ in range(n)]
array.sort()

data = [array[0][1]]
for i in range(1, n):
    if data[-1] < array[i][1]:
        data.append(array[i][1])
    else:
        data[bisect_left(data, array[i][1])] = array[i][1]

print(n - len(data))
