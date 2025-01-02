n = int(input())

array = list(map(int, input().split()))[:n]

d = [0] * n

for i, a in enumerate(array):
    d[i] = max(d[i], a)
    
    if (i + 1) >= (len(array) - 1):
        break

    for j in range(i + 2, len(array)):
        d[j] = max(d[j], array[j] + a)


print(max(d))
