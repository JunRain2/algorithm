import heapq

n = int(input())
array = []
for _ in range(n):
    s, t = map(int, input().split())
    array.append((s, t))

array.sort()
q = []  # end만 저장
heapq.heappush(q, array[0][1])
result = 1
for i in range(1, n):
    start, end = array[i]
    if q and start < q[0]:  # 제일 작은 값을 봄 -> peek()와 같은 역할
        heapq.heappush(q, end)
        result = max(result, len(q))
    else:
        heapq.heappop(q)
        heapq.heappush(q, end)

print(result)
