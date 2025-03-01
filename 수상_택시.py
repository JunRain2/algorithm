n, m = map(int, input().split())
reverse_intervals = []

# 역방향 승객만 분리하여 (목적지, 출발지) 형태로 저장
for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        reverse_intervals.append((b, a))

# 출발지(두 번째 원소)를 기준으로 내림차순 정렬하여 큰 출발지부터 탐색
reverse_intervals.sort(key=lambda x: x[1], reverse=True)

# 초기 기본 이동 거리는 m (0에서 M까지 가야 하므로)
result = m

if reverse_intervals:
    # 첫 번째 역방향 구간을 기준으로 병합 시작:
    curr_low, curr_high = reverse_intervals[0]
    for dest, start in reverse_intervals[1:]:
        # 현재 병합된 구간과 겹치는 경우: 새 승객의 출발지가 현재 그룹의 최소 목적지보다 크거나 같으면 병합 가능
        if start >= curr_low:
            curr_low = min(curr_low, dest)
        else:
            # 겹치지 않는 경우, 현재 병합된 구간에 대해 추가 detour 비용을 계산 (구간 길이의 2배)
            result += 2 * (curr_high - curr_low)
            curr_low, curr_high = dest, start
    # 마지막 병합된 구간에 대한 비용 추가
    result += 2 * (curr_high - curr_low)

print(result)
