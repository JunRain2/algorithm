import heapq

n = int(input())
# 주유소 거리, 채울 수 있는 연료의 양
array = [tuple(map(int, input().split())) for _ in range(n)]
array.sort()

l, p = map(int, input().split())
array += [(l, 0)]
q = []

result = 0
prev = 0
for a, b, in array:
    p -= (a - prev)
    while p < 0 and q:
        p -= heapq.heappop(q)
        result += 1
    if p < 0:
        print(-1)
        exit()
    
    prev = a
    heapq.heappush(q, -b)

print(result)