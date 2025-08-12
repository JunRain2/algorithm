n = int(input())

array = list()
for _ in range(n):
    name, score = input().split()
    array.append((name, int(score)))

array.sort(key=lambda x: x[1])

for a in array:
    print(a[0], end=" ")
