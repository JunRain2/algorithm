from itertools import combinations

n, c = map(int, input().split())
array = list()

for _ in range(n):
    array.append(int(input()))
array.sort()

max_value = 0
for i in combinations(array, c):
    min_value = int(1e9)
    for j in range(c - 1):
        min_value = min(min_value, abs(i[j] - i[j + 1]))
    max_value = max(max_value, min_value)

print(max_value)
