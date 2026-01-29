# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def seperate(i):
	result = []
	s = ''
	for c in i:
		if c == '+' or c == '-' or c == '*':
			result.append(int(s))
			s = ''
			result.append(c)
		else:
			s += c
	
	result.append(int(s))
	return result

def calculate(arr):
	result = []
	for i in range(0, len(arr), 2):
		if arr[i] == '+':
			result.append(arr[i + 1])
		elif arr[i] == '-':
			result.append(-arr[i + 1])
		elif arr[i] == '*':
			v = result.pop()
			result.append(v * arr[i + 1])
			
	return sum(result)

a, b = input().split()

a = seperate(a)
a = ['+'] + a
b = seperate(b)
b = ['+'] + b

print(max(calculate(a), calculate(b)))