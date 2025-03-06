# 도시의 개수
n = int(input())
load = list(map(int, input().split()))
prices = list(map(int, input().split()))

dist = load[n - 2]
result = 0
m = min(prices[: n - 1])
for i in range(n - 2, 0, -1):
    if prices[i] > m:
        dist += load[i - 1]
        continue
    result += dist * m
    m = min(prices[: n - i - 1])
    dist = load[i - 1]

result += prices[0] * dist
print(result)
