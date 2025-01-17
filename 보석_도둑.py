import heapq

n, k = map(int, input().split())

data = []
for _ in range(n):
    m, v = map(int, input().split())  # 무게, 가격
    data.append((m, v))

data.sort(key=lambda x: (-x[1], -x[0]))

backpack = []
for _ in range(k):
    heapq.heappush(backpack, -int(input()))  # 최대 무게


result = 0
weight = -heapq.heappop(backpack)
for m, v in data:
    if weight >= m:
        result += v
        if not backpack:
            break
        weight = -heapq.heappop(backpack)

print(result)
