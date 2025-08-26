# 각 폭격 미사일의 x 좌표 범위 목록 targets
def solution(targets):
    # 종료점 기준으로 정렬
    targets = sorted(targets, key=lambda x: x[1])
    
    count = 0
    last_end = 0
    
    for start, end in targets:
        # 이전에 선택한 구간의 끝점보다 시작점이 크거나 같으면 겹치지 않음
        if start >= last_end:
            count += 1
            last_end = end
            
    return count

"""
end를 통해 정렬 -> 기준점을 end로 잡아둠, 먼저 나오는 수는 이전 end보다 무조건 작다
start를 통한 비교 
"""