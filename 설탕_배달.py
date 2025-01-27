n = int(input())

d = [int(1e9)] * 50001

d[0] = 0
for i in range(3, n + 1):
    d[i] = min(d[i - 3], d[i - 5]) + 1

if d[n] >= int(1e9):
    print(-1)
else:
    print(d[n])
