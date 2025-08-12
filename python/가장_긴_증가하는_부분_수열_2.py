from bisect import bisect_left

n = int(input())
data = list(map(int, input().split()))
array = [data[0]]

for i in range(1, n):
    if data[i] > array[-1]:
        array.append(data[i])
    else:
        index = bisect_left(array, data[i])
        array[index] = data[i]

print(len(array))
