n, m, k = map(int, input().split())
arr = list(map(int, input().split()))[:n]

arr.sort(reverse=True)

result = 0
cnt = k
for _ in range(m):
    if cnt <= 0:
        result += arr[1]
        cnt = k
    else:
        cnt -= 1
        result += arr[0]

print(result)
