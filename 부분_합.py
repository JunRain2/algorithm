n, m = map(int, input().split())
data = list(map(int, input().split()))

start, end = 0, 1
result = n
for i in range(n):
    if sum(data[start:end]) < m:
        end += 1
    else:
        while sum(data[start:end]) >= m:
            result = min(result, end - start)
            start += 1
if result == n:
    print(-1)
else:
    print(result)