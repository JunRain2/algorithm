n, m = map(int, input().split())
list = list()

d = [0] * 10001

for _ in range(n):
    i = int(input())
    list.append(i)

for i in range(0, m + 1):
    for j in list:
        if d[i + j] == 0:
            d[i + j] = d[i] + 1
        else:
            d[i + j] = min(d[i + j], d[i] + 1)

result = d[n] if d[n] == 0 else -1
print(result)
