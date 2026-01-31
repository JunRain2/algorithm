answer = list(map(int, list(input())))
user = list(map(int, list(input())))

def check(arr):
	result = [0, 0, 0, 0]
	
	for i in range(4):
		if arr[i] == answer[i]: # 스트라이크인 경우
			result[i] = 1
		elif arr[i] in answer: # 볼인 경우
			result[i] = 2
		else:
			result[i] = 3

	return result

def check_same_num(index):
	n = user[index]
	for i in range(4):
		if i == index:
			continue
		if user[i] == n: # 같은 수가 존재하는 경우
			return True
	# 같은 수가 존재하지 않는 경우
	return False

def second(user, status):
	for i in range(4):
		if status[i] == 1:
			continue
		elif status[i] == 3:
			# 1을 더한 뒤 10을 나눔
			user[i] = (user[i] + 1) % 10
			# 계산한 값이 다른 자리에 존재한다면 존재하지 않을 때까지 반복
			while check_same_num(i):
				user[i] = (user[i] + 1) % 10

	return user
				
def is_ball(status):
	for i in range(4):
		if status[i] == 2:
			return True
	return False

def move(user, status):
	current = None
	for i in range(4):
		if status[i] != 1:
			if current == None:
				current = user[i]
			else:
				user[i], current = current, user[i]

	for i in range(4):
		if status[i] != 1:
			user[i] = current
			break

	return user

result = 1
while answer != user: # 승리인지 판단
	status = check(user)
	user = second(user, status) # 2번 규칙 수행

	# 3번 규칙 수행
	# 볼이 하나라도 존재하는 경우
	if is_ball(status):
		user = move(user, status)

	result += 1

print(result)

"""
"2번 과정에서 Ball인 자리가 있었다면, ~~" 이렇게 표기하는게 맞냐?
1번 과정에서 판단한 자리 값 기준으로 풀이하는건데 2번 과정~~~라고 하니깐 틀리지
"""