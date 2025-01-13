n = int(input())
data = list()
for _ in range(n):
    data.append(int(input()))

total = 0
for i in range(n - 1):
    data.sort()
    x, y = data.pop(0), data.pop(0)
    total += x + y
    data.append(x + y)

print(total)
