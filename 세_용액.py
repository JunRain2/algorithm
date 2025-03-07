n = int(input())
array = list(map(int, input().split()))
array.sort()

result = []
value = int(1e11)
for start in range(n):
    left = start + 1
    right = n - 1
    while left < right:
        tmp = [array[start], array[left], array[right]]
        v = sum(tmp)
        if abs(v) < value:
            result = tmp
            value = abs(v)
        if v < 0:
            left += 1
        else:
            right -= 1

print(*sorted(result))