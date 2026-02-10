n = int(input())

lines = [tuple(map(int,input().split())) for _ in range(n)]
lines.sort()

result = 0

start, end = lines[0]
for x, y in lines:
    if start <= x <= end:
        start, end = min(start, x), max(end, y)
    else:
        result += abs(end - start)
        start, end = x, y

result += abs(end - start)
    
print(result)