import heapq

# 입력 받기
n = int(input().strip())
stations = [tuple(map(int, input().split())) for _ in range(n)]
l, p = map(int, input().split())

# 주유소를 위치 기준 (오름차순) 정렬하고, 목적지(연료 0) 추가
stations.sort()
stations.append((l, 0))

# 현재 연료는 초기 연료 p로 바로 할당
currentFuel = p
prev = 0        # 이전 주유소(또는 출발점)의 위치
refuelCount = 0 # 정류 횟수
maxHeap = []    # 지금까지 지나친 주유소 중 연료를 최대 힙으로 관리

# 각 주유소(목적지 포함)에 대해 시뮬레이션
for location, fuel in stations:
    # 현재 주유소까지 이동하는 데 필요한 연료 소모량
    gap = location - prev
    currentFuel -= gap

    # 만약 현재 연료로 도달할 수 없다면,
    # 지금까지 들렀던 주유소들 중 가장 연료가 많은 곳에서 보충한다.
    while currentFuel < 0:
        # 보충 가능한 주유소가 없다면 도달 불가능
        if not maxHeap:
            print(-1)
            exit()
        # 최대 힙에서 주유량이 가장 큰 주유소의 연료를 보충
        currentFuel += -heapq.heappop(maxHeap)
        refuelCount += 1

    # 현재 주유소의 연료 정보를 최대 힙에 추가 (최대 힙을 위해 음수로 저장)
    heapq.heappush(maxHeap, -fuel)
    prev = location

print(refuelCount)