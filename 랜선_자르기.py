k, n = map(int, input().split()) # 가지고 있는 랜선, 필요한 랜선
array = [int(input()) for _ in range(k)]
array.sort()

start = 1
end = sum(array) // n

result = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in array:
        cnt += i // mid
    
    if cnt >= n:
        start = mid + 1
        result = max(result, mid)
    else:
        end = mid - 1
        
print(result)