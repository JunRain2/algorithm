n = int(input())
data = list(map(int, input().split()))

s = []
result = [-1] * n
for i, item in enumerate(data):
    if not s:
        s.append((i, item))
        continue
    while s and s[-1][1] < item:
        a, b = s.pop()
        result[a] = item
    s.append((i, item))
    
print(*(result))