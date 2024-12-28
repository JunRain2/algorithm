n, m = map(int, input().split())

max = 0
for _ in range(n):
    arr = list(map(int, input().split()))[:m]
    min_value = min(arr)
    max = max(max, min_value)
    
print(max)
