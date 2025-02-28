import heapq

n, m = map(int, input().split())

data = dict()
for i in range(n):
    # 무게, 가격
    a, b = map(int, input().split())
    if b not in data:
        data[b] = list()
    heapq.heappush(data[b], -a)

k = sorted(data.keys())
s = 0
for i in range(len(k) - 1):
    s -= heapq.heappop(data[k[i]]) # 현재 가격 중 제일 무거운 고기
    if s >= m:
        print(k[i])
        exit()
    s -= sum(data[k[i]]) # 남은 고기

s -= heapq.heappop(data[k[-1]])
if s >= m:
    print(k[-1])
    exit()

print(-1)