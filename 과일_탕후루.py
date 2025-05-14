from collections import defaultdict

n = int(input())
data = list(map(int, input().split()))

count = defaultdict(int)
left = 0
max_len = 0

for right in range(n):
    count[data[right]] += 1

    while len(count) > 2:
        count[data[left]] -= 1
        if count[data[left]] == 0:
            del count[data[left]]
        left += 1

    max_len = max(max_len, right - left + 1)

print(max_len)