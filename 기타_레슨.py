n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 1
end = sum(array)

result = sum(array)
while start <= end:
    cnt = 1
    mid = (start + end) // 2  # 최대값 찾기
    tmp = 0
    for i in array:
        tmp += i
        if tmp > mid:
            cnt += 1
            tmp = i

    if cnt > m:
        start = mid + 1
    else:
        end = mid - 1
        result = min(result, mid)

print(result)
