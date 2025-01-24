n = int(input())
k = int(input())

array = [0]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        array.append(i * j)

array.sort()
print(array[k])

start, end = 1, n**2

while start <= end:
    mid = (start + end) // 2
    