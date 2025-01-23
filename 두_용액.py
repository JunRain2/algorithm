n = int(input())
array = list(map(int, input().split()))
array.sort()
result = [0, 0]

start_idx = 0
end_idx = n - 1
gap = int(2*1e9)
while start_idx < end_idx and gap != 0:
    start, end = array[start_idx], array[end_idx]
    if gap > abs(end + start):
        result = [start, end]
        gap = abs(end + start)
    
    if end + start < 0:
        start_idx += 1
    else:
        end_idx -= 1

print(*result)
