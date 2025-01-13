n = int(input())
data = list(map(int, input().split()))[:n]

data.sort()

print(data[int(n / 2 - 1)])
