n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 1
end = max(array)

answer = 0
while start <= end:
    mid = (start + end) // 2
    h = 0
    for i in array:
        h += max(0, i - mid)
    
    if h >= m:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)