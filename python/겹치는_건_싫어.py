from collections import Counter

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = -1
cnt = Counter()

result = 0
for i in arr:
    cnt[i] += 1
    end += 1
    while cnt[i] > m:
        cnt[arr[start]] -= 1
        start += 1
        

    result = max(result, end - start + 1)

print(result)