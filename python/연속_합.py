n = int(input())
array = list(map(int, input().split()))

for i in range(1, n):
    array[i] = max(array[i - 1] + array[i], array[i])
    
print(max(array))