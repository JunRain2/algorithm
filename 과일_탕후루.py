from collections import Counter

# 2종류의 과일만 남기면서 최댓값 구하기
n = int(input())
data = list(map(int, input().split()))
left, right = 0, n - 1

counter = Counter(data)

while len(counter.keys()) > 2:
    if (counter[data[right]] - 1) == 0:
        counter[data[right]] -= 1
        right -= 1
    elif (counter[data[left]] - 1 ==0):
        counter[data[left]] -= 1
        left += 1
    
    counter += Counter()
    n -= 1

print(n)