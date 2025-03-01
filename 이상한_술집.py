n, m = map(int, input().split())

data = [int(input()) for _ in range(n)]
data.sort()

start = 1
end = max(data)

result = 0
while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in data:
        count += i // mid

    if count >= m:
        result = max(result, mid)
        start = mid + 1
    else:
        end = mid - 1

print(result)
