from collections import defaultdict
import heapq

n = int(input())
tops = list(map(int, input().split()))

buildings = defaultdict(list)

# 정방향 순회, i 기준으로 왼쪽에 머가 보이는지 
stack = []
for i in range(n):
    if not stack:
        stack.append((tops[i],i))
        continue
    
    
    prev = tops[i]
    while stack and stack[-1][0] <= prev:
        stack.pop()
        
    for _, idx in stack:
        # 거리, 인덱스 번호
        heapq.heappush(buildings[i],(abs(i - idx), idx + 1))
        
    stack.append((tops[i], i))
    
# 역방향 순회, i 기준으로 오른쪽에 머가 보이는지
stack = [] # distance, num
for i in range(n-1, -1, -1):
    if not stack:
        stack.append((tops[i],i))
        continue
    
    
    prev = tops[i]
    while stack and stack[-1][0] <= prev:
        stack.pop()
    
    for _, idx in stack:
        # 거리, 인덱스 번호
        heapq.heappush(buildings[i],(abs(i - idx), idx + 1))
    
    stack.append((tops[i], i))

for i in range(n):
    if not buildings[i]:
        print(0)
    else:
        print(len(buildings[i]), heapq.heappop(buildings[i])[1])