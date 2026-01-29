# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 이진트리는 "정렬된" 상태에서 사용해야하는데;;; 정신을 바짝차리자

n = int(input())
arr = list(map(int ,input().split()))

result = arr[0]

# 처음에는 오르막길 검사
i = 1
prev = arr[0]
while i < n:
	if prev > arr[i]:
		break

	result += arr[i]
	prev = arr[i]
	i += 1

while i < n:
	if prev < arr[i]:
		result = 0
		break

	result += arr[i]
	prev = arr[i]
	i += 1


print(result)