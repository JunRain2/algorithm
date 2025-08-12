n = int(input())  # 센서 개수
k = int(input())  # 집중국 개수
positions = list(map(int, input().split()))

if k >= n:
    print(0)
    exit()

# 센서 위치 정렬
positions.sort()

# 인접한 센서들 간의 거리 차이 저장
distances = [positions[i + 1] - positions[i] for i in range(n - 1)]

# 거리 차이 내림차순 정렬 후, 가장 큰 K-1개의 간격 제거
distances.sort(reverse=True)

# 남은 거리의 합 = 수신 거리의 최소합
print(sum(distances[k - 1:]))