def is_in_triangle(r, c, points):
    """
    점 (r, c)가 삼각형 내부 또는 경계에 있는지 확인
    외적을 이용한 삼각형 내부 판정
    """
    r1, c1 = points[0]
    r2, c2 = points[1]
    r3, c3 = points[2]
    
    # 삼각형의 세 변에 대해 외적 계산
    def sign(p1r, p1c, p2r, p2c, p3r, p3c):
        return (p1r - p3r) * (p2c - p3c) - (p2r - p3r) * (p1c - p3c)
    
    d1 = sign(r, c, r1, c1, r2, c2)
    d2 = sign(r, c, r2, c2, r3, c3)
    d3 = sign(r, c, r3, c3, r1, c1)
    
    # 모든 외적 값이 같은 부호이거나 0이면 삼각형 내부
    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
    
    return not (has_neg and has_pos)


# 입력 받기
N, Q = map(int, input().split())

# 2차원 배열 입력
arr = []
for i in range(N):
    row = list(map(int, input().split()))
    arr.append(row)

# 각 삼각형 처리
for _ in range(Q):
    coords = list(map(int, input().split()))
    r1, c1, r2, c2, r3, c3 = coords
    
    # 1-based를 0-based로 변환
    r1, c1, r2, c2, r3, c3 = r1-1, c1-1, r2-1, c2-1, r3-1, c3-1
    
    # 세 점 저장
    points = [(r1, c1), (r2, c2), (r3, c3)]
    
    # 경계 찾기
    min_r = min(p[0] for p in points)
    max_r = max(p[0] for p in points)
    min_c = min(p[1] for p in points)
    max_c = max(p[1] for p in points)
    
    total = 0
    
    # 삼각형 영역 순회
    for i in range(min_r, max_r + 1):
        for j in range(min_c, max_c + 1):
            # 점이 삼각형 내부 또는 경계에 있는지 확인
            if is_in_triangle(i, j, points):
                total += arr[i][j]
    
    print(total)