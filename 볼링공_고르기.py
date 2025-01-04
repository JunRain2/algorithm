n, m = map(int, input().split())

k = list(map(int, input().split()))[:n]

count = 0
for i in range(n):
    for j in range(n):
        if k[i] == k[j]:
            continue
        else:
            count += 1
            
print(count/2)