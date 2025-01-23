import heapq

n = int(input())
weights = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

if max(weights) < max(boxes):
    print(-1)
    exit()

boxes = [-i for i in boxes]

weights.sort(reverse=True)

result = 0
while boxes:
    tmp = []
    for w in weights:
        if not boxes:
            break
        tmp_box = -heapq.heappop(boxes)
        while tmp_box > w and boxes:
            tmp.append(-tmp_box)
            tmp_box = -heapq.heappop(boxes)
    for t in tmp:
        heapq.heappush(boxes, t)
    result += 1

print(result)
