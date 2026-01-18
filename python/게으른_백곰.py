def execute() -> int:
    n, k = map(int, input().split())
    
    # 좌표별 얼음 양 저장
    buckets = [0] * 1000001
    max_pos = 0
    
    for _ in range(n):
        g, x = map(int, input().split())
        buckets[x] += g
        max_pos = max(max_pos, x)
    
    # 윈도우 크기: 2*k + 1 (좌우 k씩)
    window_size = 2 * k + 1
    
    # 초기 윈도우 합 계산
    current_sum = sum(buckets[0:min(window_size, max_pos + 1)])
    max_ice = current_sum
    
    # 슬라이딩 윈도우로 최댓값 찾기
    for i in range(1, max_pos + 1):
        # 왼쪽 끝 제거
        if i - 1 - k >= 0:
            current_sum -= buckets[i - 1 - k]
        
        # 오른쪽 끝 추가
        if i + k <= max_pos:
            current_sum += buckets[i + k]
        
        max_ice = max(max_ice, current_sum)
    
    return max_ice

print(execute())