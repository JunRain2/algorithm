from bisect import bisect_left

n = int(input())
array = [int(input()) for _ in range(n)]

data = [array[0]]
for i in range(1, n):
    if data[-1] < array[i]:
        data.append(array[i])
    else:
        data[bisect_left(data, array[i])] = array[i]

print(n - len(data))