# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import bisect

n, m, k = map(int, input().split())

ants = list(map(int, input().split()))
honey = list(map(int, input().split()))

ants.sort()
honey.sort()


# 그리드 알고리즘
def can(distance):
	a = 0 # 현재 개미 index
	h = 0 # 현재 선택된 꿀 수 

	while a < n: # 모든 개미가 꿀 범위에 들어 갈때까지
		# 현재 개미(a)의 오른쪽, 왼쪽 범위
		left_range = ants[a] - distance
		right_range = ants[a] + distance

		# 현재 개미(a)의 반경에 가장 오른쪽에 있는 꿀 인덱스
		# right_range의 값이 들어갈 인덱스, 따라서 -1을 해야 가장 오른쪽 인덱스
		right_index = bisect.bisect_right(honey, right_range) - 1

		# 범위를 벗어난 경우
		if right_index < 0 or honey[right_index] < left_range:
			return False

		# h 범위의 꿀을 "선택"
		h += 1
		if h > k:
			return False

		# 범위에 해당하는 개미들을 포함
		while a < n and abs(ants[a] - honey[right_index]) <= distance:
			a += 1

	return True


# 개미와 꿀의 거리 범위 (좁혀나가면서 답을 찾음)
left, right = 0, max(ants[-1], honey[-1]) - min(ants[0], honey[0])
result = right 

while left <= right:
	mid = (right + left) // 2

	if can(mid):
		result = min(result, mid)
		right = mid - 1
	else:
		left = mid + 1

print(result)