n, m = map(int, input().split())
array = list(map(int, input().split()))

start = max(array)
end = sum(array)
result = end

while start <= end:
    mid = (start + end) // 2
    tmp = 0
    cnt = 1
    for x in array:
        if tmp + x > mid:
            cnt += 1
            tmp = x
        else:
            tmp += x

    if cnt <= m:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)
