import heapq

n, k = map(int, input().split())

# 보석 정보 저장
jewels = []
for _ in range(n):
    m, v = map(int, input().split())
    jewels.append((m, v))

# 가방 정보 저장
bags = []
for _ in range(k):
    bags.append(int(input()))

# 보석을 무게 기준으로 오름차순 정렬
jewels.sort()
# 가방도 오름차순 정렬
bags.sort()

result = 0
temp = []  # 현재 가방에 들어갈 수 있는 보석들의 가격을 저장할 최대 힙
j = 0  # 보석 인덱스

# 각 가방에 대해 처리
for bag in bags:
    # 현재 가방에 들어갈 수 있는 모든 보석을 힙에 넣음
    while j < n and jewels[j][0] <= bag:
        # 가격을 음수로 저장하여 최대 힙처럼 사용
        heapq.heappush(temp, -jewels[j][1])
        j += 1
    
    # 가능한 보석 중 가장 비싼 보석을 선택
    if temp:
        result -= heapq.heappop(temp)

print(result)
