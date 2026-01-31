# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# N마리 쥐의 몸집 크기의 대푯값을 추출
# [X-2, X+2] 구간에 속하는 쥐가 가장 많을 때, 그 중 가장 작은 X값이 대푯값
# 정우는 A장소의 대푯값이 B장소의 대푯값보다 더 클 것이라 기대

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

def cal(arr):
	left = right = 0
	result = 0
	max_length = 0

	# 투 포인트로 풀이
	while right < n:
		# 오른쪽과 왼쪽의 차가 4이하일 때 
		if arr[right] - arr[left] <= 4:
			# 현재 길이가 최대라면
			if max_length < right - left:
				# 대푯값 + 최대길이 업데이트
				result = (arr[right] + arr[left]) // 2 # ??? 대푯값 구하는 로직이 요상함
				max_length = right - left
			# 최대길이가 같다면
			elif max_length == (right - left):
				# 더 큰 대푯값으로 변경	
				result = min(result, (arr[right] + arr[left]) // 2)
			
			right += 1

		# 4를 초과한 경우 
		else:
			# right가 (n-1)일 경우 left를 줄이면 max_lenght가 줄어듦 -> 정답이 없음
			if right == (n - 1):
				return result
			# left 업데이트
			left += 1

	return result

a_result = cal(a)
b_result = cal(b)
print(a_result, b_result)
print("good" if a_result > b_result else "bad")
	