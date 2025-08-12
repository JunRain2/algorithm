from collections import defaultdict
import heapq

n = int(input())

data = defaultdict(list)
for _ in range(n):
    # 과제 마감일까지 남은 일수, 과제의 점수
    d, w = map(int, input().split())
    heapq.heappush(data[d], -w)

result = []
for day in sorted(data.keys()):
    weight = -heapq.heappop(data[day])
    heapq.heappush(result, weight)
    while data[day]:
        weight = -heapq.heappop(data[day])
        if len(result) < day:
            heapq.heappush(result, weight)
        elif weight > min(result):
            heapq.heappop(result)
            heapq.heappush(result, weight)
        else:
            break

print(sum(result))
