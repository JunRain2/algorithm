n = int(input())
data = list(map(int, input().split()))[:n]

data.sort()

print(data[(n - 1) // 2])
