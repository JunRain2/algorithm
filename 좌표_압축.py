from bisect import bisect_left

n = int(input())
array = list(map(int, input().split()))
set_array = list(set(array))
set_array.sort()

result = []

for i in array:
    result.append(bisect_left(set_array, i))

print(*result)
