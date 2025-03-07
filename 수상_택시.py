n, m = map(int, input().split())

data = []
for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        data.append((b, a))

result = m 
data.sort(key=lambda x: (x[0], -x[1]))

a = b = 0
for x, y in data:
    if a <= x <= b:
        b = max(b, y)
    else:
        result += (b - a) * 2
        a, b = x, y
        
result += (b - a) * 2
print(result)