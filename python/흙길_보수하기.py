"""
N개의 물웅덩이 
길이가 L인 널판지
물웅덩이 위치와 크기가 주어졌을 때 이를 덮기 위한 널판지의 최소 개수
"""

n, l = map(int, input().split())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))
    
arr.sort()

cnt = 0
current = 0
for start, end in arr:
    while current < end:
        current = max(start, current) + l
        cnt += 1

print(cnt)