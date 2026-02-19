"""
1. 학생들이 추천을 시작하기 전에 모든 사진틀은 비어있다.
2. 어떤 학생이 특정 학생을 추천한다면, 추천받은 학생의 사진이 반드시 사진틀에 게시
3. 비어 있는 사진 틀이 없는 경우, 추천 받은 횟수가 가장 적은 학생의 사진을 제거, 
    그 자리에 새롭게 추천받은 학생의 사진을 게시, 타이브레이커시 오래된 사진을 제거
4. 추천 받은 경우, 추천 받은 횟수만 증가시킨다.
5. 게시된 사진이 삭제되는 경우 해당 학생이 추천받은 횟수는 0으로 변경
"""

n = int(input()) # 사진 틀의 수
r = int(input())
arr = list(map(int, input().split()))

photos = dict() # (추천 수, 나이)

for p in arr:
    # p가 photos에 포함되어 있다면
    if p in photos.keys():
        # p의 추천 수를 증가 시킴
        photos[p] = (photos[p][0] + 1, photos[p][1])
    # 아니라면
    else:
        # 사진첩이 n명 이상이라면
        if len(photos.keys()) >= n:
            # 제일 추천 수가 적으면서 나이가 많은 사진 제거
            candidate = min(photos.values())
            
            for k in list(photos.keys()):
                if photos[k] == candidate:
                    del photos[k]
                    
        photos[p] = (1, 0)
        
    # 현재 사진첩의 나이를 1씩 증가시킴
    for k in list(photos.keys()):
        photos[k] = (photos[k][0], photos[k][1] -1)

print(*list(sorted(list(photos.keys()))))