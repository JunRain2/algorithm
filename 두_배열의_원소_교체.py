n, k = map(int, input().split())

a = list(map(int, input().split()))[:n]
b = list(map(int, input().split()))[:n]

a.sort()
b.sort(reverse= True)

for i in range(k):
    a[i], b[i] = b[i], a[i]
    
print(sum(a))