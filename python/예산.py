n = int(input())
array = list(map(int, input().split()))
asset = int(input())

array.sort()

start = 1
end = max(array)

result = 0
while start <= end:
    mid = (start + end) // 2
    tmp = 0
    for i in array:
        if mid > i:
            tmp += i
        else:
            tmp += mid
    if tmp > asset:
        end = mid - 1
    else:
        start = mid + 1
        result = max(mid, result)
        
print(result)