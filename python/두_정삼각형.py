# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

# a와 b 비교
def diff(a, b):
	result = 0
	for i in range(n):
		for j in range(i + 1):
			result += abs(a[i][j] - b[i][j])

	return result


# 좌-우 반전
def reverse(t):
	for i in range(n):
		t[i].reverse()
	return t


#          (0,0)
#        (1,0)(1,1)
#     (2,0)(2,1)(2,2)
#   (3,0)(3,1)(3,2)(3,3)     (n - 1, 0) 이 root

# 우로 120
def right(t):
	result = []

	# 왼쪽 아래 새로운 root에서 열을 +1 해가면서 "대각선"으로 삽입하는 방법
	for i in range(n):
		row = n - 1
		tmp = []
		while i >= 0:
			tmp.append(t[row][i])
			i -= 1
			row -= 1
			
		result.append(tmp)
	return result
	

result = diff(a, b)

# 좌(검)좌(검) 좌-반(검) 좌(검)좌(검)
a = right(a)
result = min(result, diff(a, b))
a = right(a)
result = min(result, diff(a, b))

a = right(a)
a = reverse(a)
result = min(result, diff(a, b))

a = right(a)
result = min(result, diff(a, b))
a = right(a)
result = min(result, diff(a, b))

print(result)
