n, m = map(int, input().split())
data = list(map(int, input().split()))

start, end = 0, 0
total = 0
result = n + 1

while True:
    if total < m:
        if end == n:
            break;
        total += data[end]
        end += 1
    else:
        result = min(result, end - start)
        total -= data[start]
        start += 1
        
if result == (n + 1):
    print(0)
else:
    print(result)