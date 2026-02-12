h, w = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
for i in range(w):
    left_max = max(arr[:i+1])
    right_max = max(arr[i:])
    water = min(left_max, right_max) - arr[i]
    result += water

print(result)