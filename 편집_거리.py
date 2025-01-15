a = input()
b = input()

len_a = len(a)
len_b = len(b)

dp = [0] * 5000
# 삽입할 경우, 삭제할 경우, 업데이트 할 경우 3가지 중에서 제일 작은 값
result = int(1e9)

a_i = 0
b_i = 0
while a_i == len_a:
    if len_a > len_b: # 삽입
        a_i += 1
        b_i += 1
        len_b += 1
    elif len_a == len_b: # 업데이트
        if a[a_i] == b[b_i]:
        a_i += 1
        b_i += 1
    else : # 삭제
        b_i += 1
        len_b -= 1