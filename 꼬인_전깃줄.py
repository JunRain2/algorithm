from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))

result = 0
data = [arr[0]]

for i in range(1, n):
    if data[-1] < arr[i]:
        data.append(arr[i])
    else:
        result += 1
        idx = bisect_left(data, arr[i])
        data[idx] = arr[i]
        
print(result)