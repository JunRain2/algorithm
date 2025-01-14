n = int(input())
array = list(map(int, input().split()))

start = 0
end = n

result = -1
while start <= end:
    mid = (start + end) // 2
    if array[mid] == mid:
        result = mid
        break
    elif array[mid] > mid:
        end = mid - 1
    else:
        start = mid + 1

print(result)
