from bisect import bisect_right, bisect_left

n, x = map(int, input().split())
array = list(map(int, input().split()))[:n]

right_index = bisect_right(array, x)
left_index = bisect_left(array, x)

result = right_index - left_index

if result == 0:
    print(-1)
else :
    print(result)