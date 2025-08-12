import heapq
import sys
input = sys.stdin.readline

n = int(input())

min_h = []
max_h = []

for i in range(n):
    a = int(input())
    if len(min_h) == len(max_h):
        heapq.heappush(max_h, -a)
    else:
        heapq.heappush(min_h, a)
        
    if max_h and min_h and -1 * max_h[0] > min_h[0]:
        max_value = -1 * heapq.heappop(max_h) * 1
        min_value = heapq.heappop(min_h)
        
        heapq.heappush(max_h, -1 * min_value)
        heapq.heappush(min_h, max_value)
    
    print(max_h[0] * -1)