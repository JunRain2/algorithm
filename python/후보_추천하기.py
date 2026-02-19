from collections import deque

n = int(input())  # 사진 틀의 수
r = int(input())
arr = list(map(int, input().split()))

photos = {}      # {학생번호: 추천 수}
order = deque()  # 사진틀에 올라간 순서 (앞이 오래된 것)

for p in arr:
    if p in photos:
        photos[p] += 1
    else:
        if len(photos) >= n:
            # 추천 수가 가장 적은 학생 찾기 (동점이면 order 기준으로 오래된 것)
            min_count = min(photos[k] for k in order)
            for k in order:  # order는 오래된 순이므로 먼저 나오는 게 제거 대상
                if photos[k] == min_count:
                    order.remove(k)
                    del photos[k]
                    break

        photos[p] = 1
        order.append(p)

print(*sorted(photos.keys()))